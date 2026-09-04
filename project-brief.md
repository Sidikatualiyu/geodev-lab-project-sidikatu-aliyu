# My project brief
My project will use GIS and multi-temporal satellite imagery to assess how Minna has expanded over time. Landsat imagery will be used to reconstruct historical urban growth, while Sentinel-2 imagery will provide higher-resolution information on recent development. The final output will be a GIS-based urban growth map and analysis system showing where Minna has expanded, how rapidly it has grown, and the major spatial patterns of development.

## The question

How has urban growth in Minna, Niger State changed spatially and temporally over the past years, and where is the city experiencing the greatest expansion?

## Why it matters

Minna is expanding as population and development increase, creating pressure on land, infrastructure, vegetation, transportation and other urban resources. Mapping and measuring urban expansion will help identify the direction, rate and intensity of growth and provide useful information for urban planning and infrastructure development.

## The data I need

- Landsat satellite imagery – 30 m resolution – approximately 10–50 MB
- Sentinel-2 satellite imagery – 10 m resolution – approximately 20–100 MB 
- Minna/Niger State administrative boundaries – GRID3 – approximately 1–12 MB 
- Settlement/built-up extents – GRID3 – approximately 5–40 MB 
- Road network – OpenStreetMap – approximately 1–10 MB 
- Population data – WorldPop – approximately 5–30 MB 
- Elevation – Copernicus DEM 30 m – approximately 5–20 MB 

## Where the data comes from

- Landsat – Google Earth Engine: https://developers.google.com/earth-engine/datasets/catalog/landsat
- Sentinel-2 – Google Earth Engine: https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED
- Administrative boundaries – GRID3 Nigeria: https://grid3.org/geospatial-data-nigeria
- Settlement extents – GRID3 Nigeria: https://grid3.org/geospatial-data-nigeria
- Road network – OpenStreetMap: https://www.openstreetmap.org/
- Population – WorldPop: https://hub.worldpop.org/
- Elevation – OpenTopography/Copernicus DEM: https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.032021.4326.1

## What I will build

I will build a GIS-based urban growth monitoring system for Minna, Niger State, using multi-temporal satellite imagery to map and quantify changes in built-up areas over time. The system will identify the direction, rate and intensity of urban expansion and examine its relationship with roads, population distribution, settlements and terrain. The final product will include urban growth maps, change statistics and a GIS visualization that can support urban planning and decision-making.