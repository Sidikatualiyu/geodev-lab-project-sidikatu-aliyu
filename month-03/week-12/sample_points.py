import geopandas as gpd
import rasterio

import rasterio

with rasterio.open("data/raw/dem.tif") as src:
    facilities = gpd.read_file(
        "data/processed/health_facilities.gpkg", layer ="facilities"
        ).to_crs(src.crs)
    coords = [(p.x, p.y) for p in facilities.geometry]
    facilities["eleveation_m"] = [values[0] for values in src.sample(coords)]

print(facilities[["name", "eleveation_m"]].head())
