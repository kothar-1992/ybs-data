# Data Sources & Attribution

The merged routes dataset v2 (`routes.json`, built 2026-10-30) combines the project's own route roster and
metadata with stop data from the public sources below. This file is the attribution record for the merged
data — include it in the data repository and surface the credits in the app (e.g. Settings → About / Data
sources) when the merged dataset ships.

## 1. thantthet/YBS-Data — primary stop-data source

- **What it provided:** full stop-by-stop sequences, the stop registry (bilingual EN/MM stop names and
  coordinates), route shapes and colours for branch-variant entries — covering 92 of the 139 roster routes
  plus 24 branch variants.
- **Source:** https://github.com/thantthet/YBS-Data (community-maintained, last updated 2022-06-19;
  described by its maintainers as an improved, up-to-date version of the officially released YBS data,
  gathered from YBS-related Facebook groups/pages; validity best-effort).
- **Licence:** **CC BY-SA 4.0** (Creative Commons Attribution-ShareAlike 4.0 International).
- **Attribution (required):** "Stop data © thantthet/YBS-Data contributors, licensed under CC BY-SA 4.0 —
  https://github.com/thantthet/YBS-Data".
- **Share-alike note:** because the merged stop data derives from a CC BY-SA source, the merged dataset's
  stop layer inherits share-alike terms — if the merged `routes.json` is redistributed, it must carry this
  attribution and the same licence for the derived stop data.

## 2. YRTA open data via Open Development Myanmar — QA/reference source

- **What it provided:** the 2017 launch-network stop sequences for 53 services, used only as a
  quality-assurance diff layer (agreement/divergence measurement and renumbering detection). No YRTA stop
  records were copied into the merged dataset (the single permitted exception — isolated name-spelling
  fixes under strict criteria — matched zero cases in this build).
- **Source:** Yangon Bus Service Public Data, Yangon Region Transport Authority (YRTA) open data,
  version 0.1.14, reference date 14 January 2017, via Open Development Myanmar
  (https://data.opendevelopmentmekong.net — dataset "Yangon Bus Service Public Data").
- **Licence:** YRTA Open Data License 1.0 (copy kept with the source download in
  `data-sources/yrta/` during the build).
- **Attribution:** "Reference data: YRTA Yangon Bus Service open data (2017), via Open Development Myanmar."

## 3. Project's own data

- Route roster (139 route numbers), route names, fares, operating hours, schedules, colours and the
  terminal-only stop records for the 47 routes no public source covers are the project's own dataset
  (v1.0.0 production seed), carried forward unchanged except as documented in `BUILD_REPORT.md`.

## Lineage summary

```
routes.json v2
├── roster + route metadata ............ project dataset v1.0.0
├── stops for 92 routes + 24 variants .. thantthet/YBS-Data (CC BY-SA 4.0)
├── route shapes for variant entries ... thantthet/YBS-Data (CC BY-SA 4.0)
└── QA verification only (no data copied)  YRTA open data v0.1.14 (2017) via Open Development Myanmar
```
