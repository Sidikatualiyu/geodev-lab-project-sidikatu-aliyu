import geopandas as gpd 

minna = gpd.read_file("data/processed/minna.gpkg",)
print("CRS:", minna.crs)

