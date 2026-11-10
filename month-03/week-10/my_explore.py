import geopandas as gpd

print(gpd.list_layers("data/processed/Highway_minna.gpkg"))

Highway = gpd.read_file("data/processed/Highway_minna.gpkg", layer="Highway")

print(Highway.head())
print("Rows and columns:", Highway.shape)
print(Highway.geom_type.value_counts())
print("CRS:", Highway.crs)
print("Bounds:", Highway.total_bounds)

