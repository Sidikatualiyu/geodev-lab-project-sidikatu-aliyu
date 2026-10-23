import csv
with open("wards.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    print("Number of rows:", len(rows))
    print("Columns:", list(rows[0].keys()))

values = []
for row in rows:
    value = float(row["area_km2"])
    values.append(value)

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[pop_density_per_km2].strip()
        if raw == "":
            continue
        values.append(float(raw))
        return{
            "Smallest": min(values),
            "Largest": max(values),
            "Count": len(values)
        }
    result = inspect_column("wards.csv", "area_km2")
    pop_density_per_km2_result = inspect_column("wards.csv", "pop_density_per_km2")
    mean_temp_c__result = inspect_column("wards.csv", "mean_temp_c")

    print("pop_density_per_km2:", pop_density_per_km2_result)
    print("mean_temp_c:", mean_temp_c__result)