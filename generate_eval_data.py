import json
import os
from collections import defaultdict

# folder tempat semua file JSON kamu
folder_path = "data"  # ganti sesuai folder kamu

# simpan hasil
hasil = {}

for file_name in os.listdir(folder_path):
    print(file_name)

total_all = 0

for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        kategori_count = defaultdict(int)

        for item in data:
            kategori = item.get("category", "unknown")
            kategori_count[kategori] += 1

        total = len(data)
        total_all += total

        hasil[file_name] = {
            "total": total,
            "kategori": dict(kategori_count)
        }

# tampilkan hasil
for dataset, info in hasil.items():
    print(f"\nDataset: {dataset}")
    print(f"Total Chunk: {info['total']}")
    print("Kategori:")
    for k, v in info["kategori"].items():
        print(f"  - {k}: {v}")

print("\nTOTAL KESELURUHAN:", total_all)