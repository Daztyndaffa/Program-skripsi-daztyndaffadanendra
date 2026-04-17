from src.retrieve.bm25_search import BM25Retriever

bm25 = BM25Retriever()

query = "apa aja syarat tugas akhir"

results = bm25.search(query)

print("\nHASIL BM25:\n")

print("query =", query)
for r in results:
    print("-", r)