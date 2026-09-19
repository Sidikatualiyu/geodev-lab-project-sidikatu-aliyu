# Data notes
## GRID3 NGA - Operational LGA Boundaries
- Source: https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about
- Downloaded: 11/09/2026
- 774 features, polygon
- Columns: lga_name(test), lga_code(string), state_name(test), state_code(string)
- No nulls in lga_name
- Covers my LGA fully

## OSM roads 
- Query: highway = within minna (Chanchaga and Bosso LGAs)
- Extracted: 11/09/2026 via QuickOSM, highway =*
- 9,651 features, lines
- Many have no surface tag, so paved and unpaved cannot be separated everywhere
- Coverage looks good in the built-up area, sparse at the edges. 
- COMPLETENESS: Good in built-up areas, sparse at the edge
- CURRENCY:
- POSITIONAL: Roads align well with shapefile, no visible offset
- ATTRIBUTE:
- FITNESS: 
## CRS and Preparation
- All source layers arrived in EPSG: 4326
- LStudy area: Minna, extracted from GRID3 LGAs
- All layers clipped to study area, then reprojected to EPSG:32631 (UTM 31N)
- Area check: Minna 6784km2 matches published figure
- Working files in data/processed/, raw files untouched. 
