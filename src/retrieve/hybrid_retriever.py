from src.retrieve.vector_search import vector_search
from src.retrieve.bm25_search import BM25Retriever

bm25 = BM25Retriever()

def hybrid_retrieve(query, k=5):

    vector_results = vector_search(query)["documents"][0]
    bm25_results = bm25.search(query)

    scores = {}

    # BM25 lebih berat
    for i, doc in enumerate(bm25_results):
        scores[doc] = scores.get(doc, 0) + (k - i) * 0.7

    # Vector lebih ringan
    for i, doc in enumerate(vector_results):
        scores[doc] = scores.get(doc, 0) + (k - i) * 0.3

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [doc for doc, score in ranked[:k]]