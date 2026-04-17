from src.retrieve.vector_search import vector_search

query = "apa aja syarat tugas akhir"

results = vector_search(query)

print("\nHASIL RETRIEVAL (Vector Search):\n")

print("query =", query)

for doc in results["documents"][0]:
    print("-", doc)