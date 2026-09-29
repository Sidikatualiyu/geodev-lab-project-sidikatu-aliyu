# Data notes
## GADM Country data (version 4.1) - Levels 0, 1 and 2
- Source: https://gadm.org/download_country.html 
- Downloaded: 27/09/2026
- 775 features, polygon
- Columns: fid (Integer64), Name_1(text-string), Name_2(text-string), Varname_2(text-string)
- No nulls in lga_name
- Covers my LGAs fully

##GRID3 Settlement Extent 
-Source: https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about
-Downloaded: 29/09/2026
-10380 features (After clipping to study area)
-Columns: fid (Integer64bit), building_count(integr32), building_area(Decimal(double)), extent_type(text-string)
No null in the data
Covers my LGAs fully


## OSM roads 
- Query: highway = within minna (Chanchaga and Bosso LGAs)
- Extracted: 27/09/2026 via QuickOSM, highway =*
- 14,111 features, lines
- Many have no surface tag, so paved and unpaved cannot be separated everywhere
- Coverage looks good in the built-up area, sparse at the edges.
- COMPLETENESS: Good in built-up areas, sparse at the edge.
- CURRENCY: Most edits are between 2014 - 2026, new roads in minna town are present
- POSITIONAL: Roads align well with satellite imagery, no visible systematic offset.
- ATTRIBUTE: 18% of highways are unclassified, others classified as track, secondary, primary, residential, path, foothway and bridleway. 
- FITNESS: Adequate for urban growth assessment in Minna.

## CRS and Preparation
- All source layers arrived in EPSG: 4326
- Study area: Minna, extracted from GADM LGAs
- All layers clipped to study area, then reprojected to EPSG:32632 (UTM 32N)
- Area check: Minna 1657km2 matches published figure
- Working files in data/processed/, raw files untouched. 
