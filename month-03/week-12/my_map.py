import numpy as np
import rasterio
import matplotlib.pyplot as plt

with rasterio.open("data/processed/ndvi_minna.tif") as src:
    ndvi = src.read(1).astype("float32")
    nodata = src.nodata

ok = np.isfinite(ndvi) & (ndvi != nodata)

low = round(float(ndvi[ok].min()), 3)
high = round(float(ndvi[ok].max()), 3)
mean = round(float(ndvi[ok].mean()), 3)
print("NDVI range:", low, "to", high)
print("Mean NDVI:", mean)

with open("data/processed/ndvi_stats.csv", "w") as f:
    f.write("min,max,mean\n")
    f.write(str(low) + "," + str(high) + "," + str(mean) + "\n")
print("Saved data/processed/ndvi_stats.csv")

show = np.where(ok, ndvi, np.nan)
plt.imshow(show, cmap="RdYlGn", vmin=-0.2, vmax=0.8)
plt.colorbar(label="NDVI")
plt.title("NDVI, Minna")
plt.axis("off")
plt.savefig("month-03/week-12/my_map.png", dpi=200, bbox_inches="tight")
print("Saved month-03/week-12/my_map.png")