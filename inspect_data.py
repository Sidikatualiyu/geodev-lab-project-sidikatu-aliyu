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

import csv
with open("wards.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

values = []
for row in rows:
    raw = row["area_km2"].strip()
    if raw == "":
        continue
    values.append(float(raw))

print("Smallest:", min(values))
print("Largest:", max(values))
print("Count:", len(values))

import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
        return{
            "Smallest": min(values),
            "Largest": max(values),
            "Count": len(values)
        }
result = inspect_column("wards.csv", "area_km2")
print(result)

area_result = inspect_column("wards.csv", "area_km2")
pop_result = inspect_column("wards.csv", "population")

print("area:", area_result)
print("population:", pop_result)
