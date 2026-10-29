#!/usr/bin/env python3
"""Validate YBS route data and refresh manifest.json checksum/routeCount.

Usage: python3 tools/validate_and_update_manifest.py
Run from the ybs-data repo root. Exits non-zero if validation fails.
The checksum is ALWAYS generated here — never hand-edit it in manifest.json.
"""
import hashlib, json, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
routes_path = root / "routes.json"
manifest_path = root / "manifest.json"

raw = routes_path.read_bytes()
try:
    data = json.loads(raw)
except json.JSONDecodeError as e:
    print(f"FAIL: routes.json is not valid JSON: {e}")
    sys.exit(1)

routes = data.get("routes")
if not isinstance(routes, list) or not routes:
    print("FAIL: routes.json has no 'routes' list")
    sys.exit(1)

errors, ids = [], set()
for i, r in enumerate(routes):
    for field in ("id", "routeNumber", "nameEn", "nameMm", "farePrice", "stops"):
        if field not in r:
            errors.append(f"route #{i} ({r.get('id','?')}): missing {field}")
    if r.get("id") in ids:
        errors.append(f"duplicate route id: {r.get('id')}")
    ids.add(r.get("id"))
    if not r.get("stops"):
        errors.append(f"route {r.get('id')}: empty stops")

if errors:
    print("FAIL:"); [print(" -", e) for e in errors[:20]]; sys.exit(1)

checksum = hashlib.sha256(raw).hexdigest()
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest["checksum"] = f"sha256-{checksum}"
manifest["routeCount"] = len(routes)
manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(f"OK: {len(routes)} routes valid. manifest checksum + routeCount updated.")
