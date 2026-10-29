# YBS Guide — Route Data

Public data repository for YBS Guide app automatic route updates.

## Files
- `manifest.json` — version metadata, checksum, route count
- `routes.json` — full YBS route dataset (139 routes, JSON format)

## Update Process
1. Edit `routes.json` with corrected/new route data
2. Run: `Get-FileHash routes.json -Algorithm SHA256`
3. Update `manifest.json` version, checksum, lastUpdated, routeCount
4. Commit and push to main branch
5. App auto-syncs within 24 hours on next launch

## Schema
See `schema/route_template.json` in the main app repository.
