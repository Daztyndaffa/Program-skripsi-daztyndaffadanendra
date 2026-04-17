from rank_bm25 import BM25Okapi
from src.utils.loader import load_json_dataset
from src.config.settings import DATA_PATH


class BM25Retriever:

    def __init__(self):

        print("Loading dataset for BM25...")

        documents = load_json_dataset(DATA_PATH)

        self.texts = [doc["text"] for doc in documents]
        self.ids = [doc["id"] for doc in documents]

        tokenized_corpus = [text.lower().split() for text in self.texts]

        self.bm25 = BM25Okapi(tokenized_corpus)

    def search(self, query, k=5):

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            list(zip(self.texts, scores)),
            key=lambda x: x[1],
            reverse=True
        )

        return [doc for doc, score in ranked[:k]]