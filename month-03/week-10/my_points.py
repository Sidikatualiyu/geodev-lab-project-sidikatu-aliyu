import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

facilities = pd.read_csv("data/raw/health_facilities.csv")

before = (facilities["type"] == "Primary Health Centre").sum()
print("Primary Health Centre before cleaning:", before, "of", len(facilities))

def clean_type(name):
    return name.strip().replace("PHC", "Primary Health Centre")
facilities["cleaned_type"] = facilities["type"].apply(clean_type)

after = (facilities["cleaned_type"] == "Primary Health Centre").sum()

print("Primary Health Centre after cleaning:", after, "of", len(facilities))
print(facilities[["type", "cleaned_type"]])

# Turn the table into points
facilities = facilities.dropna(subset=["longitude", "latitude"])
points = gpd.GeoDataFrame(
    facilities,
    geometry=gpd.points_from_xy(facilities["longitude"], facilities["latitude"]),
    crs="EPSG:4326",
)

fig, ax = plt.subplots(figsize=(12, 10))
points.plot(ax=ax, column="cleaned_type", markersize=40, legend=True,
            legend_kwds={"title": "Facility type", "loc": "lower right"})
ax.set_title("Health facilities")
ax.set_axis_off()

fig.savefig("month-03/week-10/health_facilities_map.png", dpi=150, bbox_inches="tight")
print("Map saved")