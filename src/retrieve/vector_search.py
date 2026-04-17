import chromadb
from chromadb.utils import embedding_functions

from src.config.settings import *


def vector_search(query):

    embedding_function = embedding_functions.OllamaEmbeddingFunction(
        url=OLLAMA_HOST,
        model_name=EMBED_MODEL
    )

    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function
    )

    results = collection.query(
        query_texts=[query],
        n_results=5,
        include=["documents", "distances"]
    )

    return results