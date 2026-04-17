import ollama
import numpy as np

from src.rag.query_pipeline import process_query


# ===============================
# EMBEDDING (LOKAL)
# ===============================
def get_embedding(text):
    response = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )
    return response["embedding"]


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# ===============================
# DATA EVALUASI
# ===============================
test_queries = [
    {
        "original": "apa aja sih syarat ngambil TA",
        "expected": "apa syarat mengambil tugas akhir"
    },
    {
        "original": "kapan uts",
        "expected": "kapan ujian tengah semester"
    },
    {
        "original": "cara daftar kp gimana",
        "expected": "bagaimana cara mendaftar kerja praktek"
    },
    {
        "original": "prodi apa aja sih yang ada di fakultas teknik uir",
        "expected": "prodi apa saja yang terseida di fakultas teknik uuniversitas islam riau"
    },
    {
        "original": "berapa biaya ukt uir",
        "expected": "berapa biaya UKT Universitas Islam Riau"
    }
]


# ===============================
# EVALUATION
# ===============================
def evaluate_pipeline():

    scores = []

    print("\n===== EVALUASI QUERY PIPELINE =====\n")

    for i, data in enumerate(test_queries):

        original = data["original"]
        expected = data["expected"]

        result = process_query(original)
        processed = result["processed"]

        emb_processed = get_embedding(processed)
        emb_expected = get_embedding(expected)

        sim = cosine_similarity(emb_processed, emb_expected)

        scores.append(sim)

        print(f"Test {i+1}")
        print("Original  :", original)
        print("Processed :", processed)
        print("Expected  :", expected)
        print("Similarity:", round(sim, 4))
        print("-" * 50)

    avg_score = np.mean(scores)

    print("\n===== RATA-RATA =====")
    print("Similarity:", round(avg_score, 4))


# ===============================
# MAIN
# ===============================
if __name__ == "__main__":
    evaluate_pipeline()