#!/usr/bin/python
import catolib
import logging
import json
import concurrent.futures
import threading
import sys
import os
import sqlite3
import urllib.request
import zipfile

############ ENV Settings ############
logging.basicConfig(filename="download-schema.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s')
options = catolib.initParser()

# Increase recursion limit for complex schemas
sys.setrecursionlimit(5000)

def build_site_location_db():
    """
    Downloads geonames data and builds a SQLite database for siteLocation queries.
    Downloads cities1000.zip, countryInfo.txt, admin1CodesASCII.txt, and ISO 3166-2 data,
    processes them into a SQLite database with proper ISO state codes, then cleans up.
    """
    print("\n• Building site location database from geonames...")

    # Paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_output_path = os.path.join(script_dir, "..", "catocli", "parsers", "custom", "query_siteLocation", "siteLocation.db")
    db_output_path = os.path.normpath(db_output_path)

    # Temp files
    cities_zip = os.path.join(script_dir, "cities1000.zip")
    cities_txt = os.path.join(script_dir, "cities1000.txt")
    country_info = os.path.join(script_dir, "countryInfo.txt")
    admin1_codes = os.path.join(script_dir, "admin1CodesASCII.txt")
    iso_3166_2_file = os.path.join(script_dir, "iso_3166_2.json")

    # URLs
    cities_url = "https://download.geonames.org/export/dump/cities1000.zip"
    country_url = "https://download.geonames.org/export/dump/countryInfo.txt"
    admin1_url = "https://download.geonames.org/export/dump/admin1CodesASCII.txt"
    iso_3166_2_url = "https://raw.githubusercontent.com/olahol/iso-3166-2.json/master/iso-3166-2.json"

    try:
        # Download files
        print("  - Downloading cities1000.zip...")
        urllib.request.urlretrieve(cities_url, cities_zip)
        print("  - Downloading countryInfo.txt...")
        urllib.request.urlretrieve(country_url, country_info)
        print("  - Downloading admin1CodesASCII.txt...")
        urllib.request.urlretrieve(admin1_url, admin1_codes)
        print("  - Downloading ISO 3166-2 subdivision data...")
        urllib.request.urlretrieve(iso_3166_2_url, iso_3166_2_file)

        # Extract cities zip
        print("  - Extracting cities1000.zip...")
        with zipfile.ZipFile(cities_zip, 'r') as zip_ref:
            zip_ref.extractall(script_dir)

        # Parse countryInfo.txt -> {countryCode: countryName}
        print("  - Parsing country info...")
        country_map = {}
        with open(country_info, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                parts = line.strip().split('\t')
                if len(parts) >= 5:
                    # Column 0: ISO code, Column 4: Country name
                    country_code = parts[0]
                    country_name = parts[4]
                    country_map[country_code] = country_name
        print(f"    Loaded {len(country_map)} countries")

        # Parse admin1CodesASCII.txt -> {"CC.ADM1": stateName}
        print("  - Parsing admin1 codes...")
        admin1_map = {}
        with open(admin1_codes, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    # Column 0: code (e.g., "US.CA"), Column 1: name
                    code = parts[0]
                    name = parts[1]
                    admin1_map[code] = name
        print(f"    Loaded {len(admin1_map)} admin1 codes")

        # Parse ISO 3166-2 data to create mapping from subdivision name to ISO code
        # Format: {"US": {"name": "United States", "divisions": {"US-CA": "California", ...}}}
        print("  - Parsing ISO 3166-2 subdivision codes...")
        iso_subdivision_map = {}  # {"CC": {"subdivision_name_lower": "CC-XX", ...}}
        with open(iso_3166_2_file, 'r', encoding='utf-8') as f:
            iso_data = json.load(f)
        for country_code, country_data in iso_data.items():
            if "divisions" in country_data:
                iso_subdivision_map[country_code] = {}
                for iso_code, div_name in country_data["divisions"].items():
                    if div_name:
                        iso_subdivision_map[country_code][div_name.lower()] = iso_code
        print(f"    Loaded ISO subdivisions for {len(iso_subdivision_map)} countries")

        # Remove existing database if present
        if os.path.exists(db_output_path):
            os.remove(db_output_path)

        # Create SQLite database
        print("  - Creating SQLite database...")
        conn = sqlite3.connect(db_output_path)
        cursor = conn.cursor()

        # Create table
        cursor.execute('''
            CREATE TABLE locations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                countryCode TEXT NOT NULL,
                countryName TEXT NOT NULL,
                stateCode TEXT,
                stateName TEXT,
                timezone TEXT,
                latitude REAL,
                longitude REAL
            )
        ''')

        # Process cities1000.txt
        # Format: geonameid, name, asciiname, alternatenames, latitude, longitude,
        #         feature_class, feature_code, country_code, cc2, admin1_code,
        #         admin2_code, admin3_code, admin4_code, population, elevation,
        #         dem, timezone, modification_date
        print("  - Processing cities1000.txt...")
        row_count = 0
        batch = []
        batch_size = 10000

        with open(cities_txt, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) < 18:
                    continue

                city = parts[1]  # name
                latitude = float(parts[4]) if parts[4] else None
                longitude = float(parts[5]) if parts[5] else None
                country_code = parts[8]
                admin1_code = parts[10]
                timezone = parts[17]

                # Look up country name
                country_name = country_map.get(country_code, country_code)

                # Build state code and look up state name
                state_code = None
                state_name = None
                if admin1_code:
                    admin1_key = f"{country_code}.{admin1_code}"
                    state_name = admin1_map.get(admin1_key)
                    if state_name:
                        # Try to get ISO 3166-2 code by matching subdivision name
                        if country_code in iso_subdivision_map:
                            state_name_lower = state_name.lower()
                            state_code = iso_subdivision_map[country_code].get(state_name_lower)
                        # Fallback to geonames format if no ISO match found
                        if not state_code:
                            state_code = f"{country_code}-{admin1_code}"

                batch.append((city, country_code, country_name, state_code, state_name, timezone, latitude, longitude))
                row_count += 1

                if len(batch) >= batch_size:
                    cursor.executemany(
                        'INSERT INTO locations (city, countryCode, countryName, stateCode, stateName, timezone, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                        batch
                    )
                    batch = []
                    print(f"    Processed {row_count} cities...")

        # Insert remaining batch
        if batch:
            cursor.executemany(
                'INSERT INTO locations (city, countryCode, countryName, stateCode, stateName, timezone, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                batch
            )

        # Create indexes
        print("  - Creating indexes...")
        cursor.execute('CREATE INDEX idx_city ON locations(city)')
        cursor.execute('CREATE INDEX idx_countryCode ON locations(countryCode)')
        cursor.execute('CREATE INDEX idx_countryName ON locations(countryName)')
        cursor.execute('CREATE INDEX idx_stateCode ON locations(stateCode)')
        cursor.execute('CREATE INDEX idx_stateName ON locations(stateName)')

        conn.commit()
        conn.close()

        # Get file size
        db_size = os.path.getsize(db_output_path) / (1024 * 1024)
        print(f"  - Database created: {db_output_path}")
        print(f"    Total cities: {row_count}")
        print(f"    Database size: {db_size:.2f} MB")

    finally:
        # Cleanup downloaded files
        print("  - Cleaning up temporary files...")
        for temp_file in [cities_zip, cities_txt, country_info, admin1_codes, iso_3166_2_file]:
            if os.path.exists(temp_file):
                os.remove(temp_file)
        print("• Site location database build complete!")

def run():
    print("Starting continuous multi-threaded schema processing...")
    
    # Cleanup previous build artifacts
    catolib.cleanupBuildArtifacts()
    
    ######################### CONTINUOUS BUILD PROCESS ##############################
    ## Single continuous process - download, parse, and generate all in one flow
    print("Downloading and processing GraphQL schema...")
    print(f"Using endpoint: {options.endpoint}")
    query = {
        'query': 'query IntrospectionQuery { __schema { queryType { name } mutationType { name } subscriptionType { name } types { ...FullType } directives { name description locations args { ...InputValue } } } }  fragment FullType on __Type { kind name description fields(includeDeprecated: true) { name description args { ...InputValue } type { ...TypeRef } isDeprecated deprecationReason } inputFields { ...InputValue } interfaces { ...TypeRef } enumValues(includeDeprecated: true) { name description isDeprecated deprecationReason } possibleTypes { ...TypeRef } }  fragment InputValue on __InputValue { name description type { ...TypeRef } defaultValue }  fragment TypeRef on __Type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name } } } } } } } }',
        'operationName': 'IntrospectionQuery'
    }
    success, introspection = catolib.send(options.api_key, query, endpoint=options.endpoint)
    if not success:
        print("ERROR: Failed to download schema")
        return
    
    # Write introspection response to file
    with open('introspection.json', 'w') as f:
        json.dump(introspection, f, indent=2)

    print("• Schema downloaded successfully")
    print("• Parsing schema with enhanced dynamic field expansion...")
    catolib.parseSchema(introspection)
    print("• Schema parsed successfully")
    print("• Generating CLI components...")
    catolib.writeCliDriver(catolib.catoApiSchema)
    print("• CLI driver generated")
    catolib.writeOperationParsers(catolib.catoApiSchema)
    print("• Operation parsers generated")
    catolib.writePayloadsJson(catolib.catoApiSchema)
    print("• Payloads manifest generated")
    catolib.writeReadmes(catolib.catoApiSchema)
    print("• README files generated")
        
    total_operations = len(catolib.catoApiSchema["query"]) + len(catolib.catoApiSchema["mutation"])
    print(f"\n Continuous build completed successfully!")
    print(f"   - Total operations generated: {total_operations}")
    print(f"   - Query operations: {len(catolib.catoApiSchema['query'])}")
    print(f"   - Mutation operations: {len(catolib.catoApiSchema['mutation'])}")
    print(f"   - Total types processed: {len(catolib.catoApiIntrospection['objects']) + len(catolib.catoApiIntrospection['enums']) + len(catolib.catoApiIntrospection['scalars'])}")

    # Build site location database from geonames data
    build_site_location_db()

if __name__ == '__main__':
    run()
