with open("wards.csv") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))
with open("wards.csv") as f:
    lines = f.readlines()
for line in lines:
    print(line.strip())
with open("wards.csv") as f:
    lines = f.readlines()
for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area = parts[1]
    print(ward, "has area", area)

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    area_hectares = area_km2 * 100
    hectares = area * 100
    print(ward, "is", area_hectares,  "hectares")

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    area_hectares = area_km2 * 100
    if area_km2 > 9:
        size = "large"  
    else:
        size = "small"
    print(ward, "is", size)

total = 0
for line in lines[1:]:
    parts = line.strip().split(",")
    area_km2 = float(parts[1])
    total = total + area_km2
print(total)