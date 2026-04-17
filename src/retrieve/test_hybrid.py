from src.retrieve.hybrid_retriever import hybrid_retrieve

query = "Apa aja syarat tugas akhir"

results = hybrid_retrieve(query)

print("\nHASIL HYBRID RETRIEVAL:\n")

print("query =", query)

for r in results:
    print("-", r)