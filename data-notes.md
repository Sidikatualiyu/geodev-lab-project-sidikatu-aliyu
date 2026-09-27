# Data notes
## GADM Country data (version 4.1) - Levels 0, 1 and 2
- Source: https://gadm.org/download_country.html 
- Downloaded: 27/09/2026
- 775 features, polygon
- Columns: fid (Integer64), Name_1(text-string), Name_2(text-string), Varname_2(text-string)
- No nulls in lga_name
- Covers my LGA fully

## OSM roads 
- Query: highway = within minna (Chanchaga and Bosso LGAs)
- Extracted: 27/09/2026 via QuickOSM, highway =*
- 9,422 features, lines
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
