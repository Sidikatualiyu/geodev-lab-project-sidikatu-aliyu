import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open("data/raw/Minna_SRTM_DEM.tif") as src:
    wards = gpd.read_file("data/processed/wards.gpkg", layer="wards").to_crs(src.crs)
    print("DEM bounds: ", src.bounds)
    print("Ward bounds:", wards.total_bounds)

    means = []
    for geom in wards.geometry:
        try:
            cells, _ = mask(src, [geom], crop=True, filled=False)
            means.append(float(cells.mean()))
        except ValueError:
            means.append(np.nan)

wards["mean_elevation_m"] = np.round(means, 1)
print("Wards inside the DEM:", int(wards["mean_elevation_m"].notna().sum()), "of", len(wards))
print(wards[["ward_name", "mean_elevation_m"]])