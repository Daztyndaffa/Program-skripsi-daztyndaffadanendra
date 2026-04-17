import os
import json
from datetime import datetime

def convert_to_text(item):
    """
    Mengubah berbagai format JSON menjadi satu field text
    """

    text_parts = []

    if "title" in item:
        text_parts.append(item["title"])

    if "content" in item:
        text_parts.append(item["content"])

    if "description" in item:
        text_parts.append(item["description"])

    if "event" in item:
        text_parts.append(f"Kegiatan akademik: {item['event']}")

    if "semester" in item:
        text_parts.append(f"Semester: {item['semester']}")

    if "start_date" in item and "end_date" in item:

        try:
            start = datetime.fromisoformat(item["start_date"]).strftime("%d %B %Y")
            end = datetime.fromisoformat(item["end_date"]).strftime("%d %B %Y")

            text_parts.append(f"Tanggal pelaksanaan: {start} sampai {end}")

        except:
            text_parts.append(f"Tanggal: {item['start_date']} sampai {item['end_date']}")

    if "steps" in item and isinstance(item["steps"], list):
        text_parts.append("Langkah-langkah:")
        for step in item["steps"]:
            text_parts.append(step)

    return " ".join(text_parts)


def load_json_dataset(data_path, debug=False):

    documents = []
    file_stats = {}

    for file in os.listdir(data_path):

        if not file.endswith(".json"):
            continue

        file_path = os.path.join(data_path, file)

        with open(file_path, "r", encoding="utf-8") as f:

            data = json.load(f)

            file_stats[file] = len(data)

            for item in data:

                text = convert_to_text(item)

                documents.append({
                    "id": item.get("id"),
                    "text": text,
                    "metadata": {
                        "title": item.get("title", ""),
                        "category": item.get("category", ""),
                        "source": item.get("source", file)
                    }
                })

    
    if debug:

        print("\n================ DATASET SUMMARY ================\n")

        for file, count in file_stats.items():
            print(f"{file} -> {count} chunks")

        print("\n-----------------------------------------------")
        print(f"Total dataset files : {len(file_stats)}")
        print(f"Total chunks loaded : {len(documents)}")

        print("\nSample chunk:")

        if documents:
            sample = documents[0]
            print("ID :", sample["id"])
            print("TEXT :", sample["text"][:200])

        print("\n================================================\n")

    return documents