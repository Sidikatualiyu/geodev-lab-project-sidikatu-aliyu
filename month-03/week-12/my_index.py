import numpy as np
import rasterio

folder = "data/raw/landsat/"
scene = "Minna"

with rasterio.open(folder + scene + "_SR_B3.tif") as src:
    green = src.read(1).astype("float32")
    profile = src.profile

with rasterio.open(folder + scene + "_SR_B4.tif") as src:
    red = src.read(1).astype("float32")

with rasterio.open(folder + scene + "_SR_B5.tif") as src:
    nir = src.read(1).astype("float32")

# The Minna files were scaled to reflectance in Earth Engine, so no scaling here
valid = np.isfinite(green) & np.isfinite(red) & np.isfinite(nir)

profile.update(dtype="float32", nodata=-9999, count=1)


def compute_index(a, b, name, out_path):
    # Normalised difference: (a - b) / (a + b)
    result = np.full(a.shape, -9999, dtype="float32")
    total = a + b
    ok = valid & (total != 0)
    result[ok] = (a[ok] - b[ok]) / total[ok]

    low = round(float(result[ok].min()), 3)
    high = round(float(result[ok].max()), 3)
    print(name, "range:", low, "to", high)
    print("Mean", name + ":", round(float(result[ok].mean()), 3))

    with rasterio.open(out_path, "w", **profile) as dst:
        dst.write(result, 1)
    print("Saved", out_path)
    return result, ok


# NDVI = (NIR - Red) / (NIR + Red)
ndvi, ndvi_ok = compute_index(nir, red, "NDVI", "data/processed/ndvi_minna.tif")

# NDWI = (Green - NIR) / (Green + NIR)
ndwi, ndwi_ok = compute_index(green, nir, "NDWI", "data/processed/ndwi_minna.tif")

water = int((ndwi[ndwi_ok] > 0).sum())
print("Pixels likely to be water (NDWI > 0):", water, "of", int(ndwi_ok.sum()))