import geopandas as gpd
import matplotlib.pyplot as plt

Highway = gpd.read_file("data/processed/Highway_minna.gpkg")
minna = gpd.read_file("data/processed/minna.gpkg")

Highway = Highway.to_crs(minna.crs)
Highway = gpd.clip(Highway, minna)

fig, ax = plt.subplots(figsize=(8,7))
minna.plot(ax=ax, color="#E6F2F3", edgecolor="#094923", linewidth=1.5)
Highway.plot(ax=ax, color="#037e8e", linewidth=0.8)
ax.set_title("Highways in Minna")
ax.set_axis_off()

fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches="tight")
print("Map saved")