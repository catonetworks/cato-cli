"""Regenerate all GraphQL artifacts from the checked-in introspection snapshot."""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import catolib


def main():
    os.chdir(ROOT / "schema")
    with open("introspection.json", encoding="utf-8") as handle:
        introspection = json.load(handle)
    catolib.cleanupBuildArtifacts()
    catolib.parseSchema(introspection)
    missing = [str(path.relative_to(ROOT))
               for operations in catolib.catoApiSchema.values()
               for name in operations
               for path in (ROOT / "models" / f"{name}.json",
                            ROOT / "queryPayloads" / f"{name}.json",
                            ROOT / "queryPayloads" / f"{name}.txt")
               if not path.is_file()]
    if missing:
        raise RuntimeError("Schema generation failed to produce: " + ", ".join(missing))
    catolib.writeCliDriver(catolib.catoApiSchema)
    catolib.writeOperationParsers(catolib.catoApiSchema)
    catolib.writePayloadsJson(catolib.catoApiSchema)
    catolib.writeReadmes(catolib.catoApiSchema)


if __name__ == "__main__":
    main()
