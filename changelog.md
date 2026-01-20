# Changelog

## 2.0.1 (2025-07-05)

### Features
- Refactored authentication to support multiple profiles in a ini format
- Added export functions for IFW and WAN rules and sections into json
- Added import function into tf module for backup and restore, adjusted to use name of section and rule instead of index in source data to align with accompanying module 

## 2.1.0 (2025-08-22)

### Features

- Optimized exception handling for bulk rule import 
- Added exception handling keyboard escape 
- Added custom settings support

## 2.1.2 (2025-08-28)

### Features

- Updated dynamic cli generator to support multi-threaded processing and fixed missing fields in sub operations
- Added support for custom documentation in cli generation process, first examples in appStats and appStatsTimeSeries

## 2.1.4 (2025-09-11)

### Features

- Added all latest APIs
- Updated bulk site export/import functions to include all nested attributes for socket_sites, interfaces, and network_ranges
- Added support for csv output for appStats, appStatsTimeSeries, accountMetrics, and socketPortMetricsTimeSeries operations with some examples in the readmes

## 2.1.6 (2025-09-15)

- Added licensing mutation support - New mutation_licensing parser for commercial license operations
- Enhanced export functionality - Added CSV export format support alongside existing JSON export for socket sites 
- Improved CSV import capabilities - Extended import functionality to support both JSON and CSV data sources for Terraform imports
- Enhanced WAN interface handling - Improved interface index formatting for better consistency (INT_X format)
- Improved network range management - Better handling of native ranges and default LAN interfaces in import/export workflows
- Updated query models - Refreshed device and events data models with latest API schema
- Code organization improvements - Reordered imports for better maintainability

## 2.1.8 (2025-09-15)

- Updated path to settings file

## 3.0.0 (2025-09-24)

- Updated eventFeed operation to support persistent marker and -run to pull events continuously
- Embedded SCIM SDK into catocli, updating authentication management to prompt for bearer token and scim baseurl, supporting the following operations:
    •  catocli scim add_members - Add members to SCIM group
    •  catocli scim create_group - Create new SCIM group  
    •  catocli scim create_user - Create new SCIM user
    •  catocli scim disable_group - Disable SCIM group
    •  catocli scim disable_user - Disable SCIM user
    •  catocli scim find_group - Find groups by display name
    •  catocli scim find_users - Find users by field/value
    •  catocli scim get_group - Get specific SCIM group
    •  catocli scim get_groups - Get all SCIM groups
    •  catocli scim get_user - Get specific SCIM user
    •  catocli scim get_users - Get all SCIM users  
    •  catocli scim remove_members - Remove members from SCIM group
    •  catocli scim rename_group - Rename SCIM group
    •  catocli scim update_group - Update SCIM group
    •  catocli scim update_user - Update SCIM user
- Updated the socket_site export/import to support csv and json to align with bulk socket site module

## 3.0.2 (2025-09-24)

- Minor fix to support import lan_lag_member in csv
- Added support for generating csv and json templates for export/import
- Fixed path issue to be OS agnostic for local template for generating templates

## 3.0.3 (2025-09-24)

- Updated manifest file to include template directory

## 3.0.4 (2025-09-26)

- Updated csv formatting for appStatsTimeSeries, and socketPortMetricsTimeSeries 

## 3.0.8 (2025-10-08)

- Added bulk import, export, and purge for scim users and groups for json and csv, as well as options to generate templates
- Updated dynamic schema generation to format examples with pretty print as well as single line json blob
- OS context aware help menus for unix vs windows, and multi-line json input for both unix and windows
- Added comprehensive timeframe examples to dynamic readme generation process (appStats, socketPortMetrics, etc)

## 3.0.18 (2025-10-09)

- Upated cli to support multi-line json input for ease of use for windows and unix
- Updated eventsFeed with marker and run, and included --append-new-line for Chronicle support
- Updated help menu formatting to be dynamic for windows powershell
- Added custom report examples in readme and help menu for appStats, and appStatsTimeSeries
- Updated custom exmaples to render properly for windows
- Minor fix for readme for eventsFeed, and exception handling in menu for configure with no -h
- Updated eventsFeed help menu to properly render on Windows systems
- Updated SCIM client removing external_id from standard client to pull from url

## 3.0.22 (2025-10-15)
- Added custom reports for query.accountMetrics, query.appStats, query.appStatsTimeSeries, query.eventsTimeSeries, query.socketPortMetrics, query.socketPortMetricsTimeSeries, updating format to human readable output
- Added -f csv for custom reports
- Updated report generation to be a part of dynamic cli generation process
- Fixed examples for socketPortMetrics

## 3.0.23 (2025-10-17)
- Merged user guide documentation into the cato-cli readmes
- Added exclusions in the generation process for problematic fields for rule management

## 3.0.24 (2025-10-17)
- Merged user guide documentation into the cato-cli readmes
- Added exclusions in the generation process for problematic fields for rule management

## 3.0.25 (2025-10-21)
- Updated appStatsTimeSeries to process bytes, updated readme to include perSecond value as false in appStatsTimeSeries, updated dynamic examples to include this value

## 3.0.26 (2025-10-21)
- Updated dynamic param generation to split out containers to separate queries to reflect API explorer

## 3.0.28 (2025-10-23)
- Updated all timeseries calls to refrence perSecond as false, and validated all examples in readme and embedded in cli help menu 
- Updated dynamic help menu structure

## 3.0.31 (2025-10-31)
- Added support for tls inspection import/export

## 3.0.32 (2025-11-03)
- Added support for wan network rules import/export

## 3.0.33 (2025-11-04)
- Added queryPaylaods to manifest file to fix windows, and added tests to main package.

## 3.0.35 (2025-11-04)
- Refactored schema ingestion process to remove specific nested aliases fixing a few complex queries
- Refactored schema ingestion process to purge and regenerate all models, sample queryPayloads, and parsers
- Embedded complete API/CLI testing suite in the cato-cli repo

## 3.0.36 (2025-11-09)
- Added minor fix for top level commands typed without -h to display help menu properly
- Updated custom test for xdr.stories to look for last 30 days fimrFrame

## 3.0.39 (2025-11-14)
- Added csv export option for popLocations and for license queries
- Fixed cli driver to not exit(1) to have automated tests run succcessfully in github test runner
- Added automated test validating exit(0) for successful test for configure setup

## 3.0.41 (2025-11-21)
- Fixed raw command to run properly, added autoamted tests
- Added SCIM settings to automated tests

## 3.0.42 (2025-11-24)
- Update parsers to support --json-file for json payload to support larger input payloads
- Added custom command for categories, added automated tests
- Added support for tab auto-complete

## 3.0.44 (2025-12-10)
- Updated to latest schema adding support for clientConnectivity, ztnaAlwaysOn, and remotePortFoward.  Updated test suite.
- Updated queryPayload processer to output proper query payloads wellformatted consistent with -t command dynamically generated

## 3.0.45 (2025-12-17)
- Added readme ENUM values for queries params for accountMetrics, appStats, appStatsTimeSeries, eventsTimeSeries, socketPortMetrics, and socketPortMetricsTimeSeries

## 3.0.47 (2025-12-29)
- Added support to override endpoint, accountID and api-token per cli operation, and updated CLI with latest schema operations 

## 3.0.48 (2026-01-03)
- Updated the schema generation to write the introspection locally to track schema changes per build
- Alphabatize parsers output in the clidriver from catolib for each build

## 3.0.50 (2026-01-08)
- Updated site export to add all new params in API for site, network range, and interface for csv and json 
- Updated the generated templates for json and csv socket_site exports

## 3.0.51 (2026-01-12)
- Added bulk site location validator for csv or json

## 3.0.52 (2026-01-14)
- Updated site export and import_site_to_tf process to accommmodate new read operations for site, network range, and interface
- Added validate_site_location site location validation
- Updated templates for csv and json to align with new format

## 3.0.53 (2026-01-16)
- Migrated export/import for sites to use names instead of ids to accommodate both existing imports as well as new creation for bulk site management.  Added csv formatting logic to clean csv for malformed data and carriage returns.
- Added input validation for csv and for json 

## 3.0.54 (2026-01-16)
- Updated export with entityLookup to retrieve 1000 records as opposed to limit of 50 which is default API behavior.

## 3.0.55 (2026-01-19)
- Update export function to use increments of 50 to paginate for large exports of sites, interfaces and ranges.

## 3.0.56 (2026-01-19)
- Updated request librtary to retry if api gateway response with timeout, 0, 15, and 30 seconds before failing. 

## 3.0.58 (2026-01-20)
- Added logic to retry API after rate limit, and added logic to populate stateCode when city is missing in api response.
- Added hard coded value for lag_min_links as 1, as this is not available in API and is a best practice value.
