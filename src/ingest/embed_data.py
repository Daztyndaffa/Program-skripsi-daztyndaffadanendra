import chromadb
from chromadb.utils import embedding_functions

from src.config.settings import *
from src.utils.loader import load_json_dataset


def embed_dataset():

    print("Loading dataset...")

    documents = load_json_dataset(DATA_PATH)

    print(f"\nTotal documents: {len(documents)}")

    # Embedding model dari Ollama
    embedding_function = embedding_functions.OllamaEmbeddingFunction(
        url=OLLAMA_HOST,
        model_name=EMBED_MODEL
    )

    # koneksi ke ChromaDB
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    ids = []
    texts = []
    metadatas = []

    for doc in documents:
        ids.append(doc["id"])
        texts.append(doc["text"])
        metadatas.append(doc["metadata"])

    print("\nEmbedding documents...")

    collection.add(
        ids=ids,
        documents=texts,
        metadatas=metadatas
    )

    print("\nEmbedding selesai!")
    print("Vector database tersimpan di folder chroma_db")


if __name__ == "__main__":
    embed_dataset()