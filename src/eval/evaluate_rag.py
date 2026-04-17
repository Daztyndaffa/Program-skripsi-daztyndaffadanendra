import os
import json
import numpy as np

# ===============================
# API KEY
# ===============================

from src.config.settings import OPENAI_API_KEY
from src.config.settings import EMBEDDING_API_KEY

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# ===============================
# LIBRARY
# ===============================

from datasets import Dataset
from ragas import evaluate

from ragas.metrics import (
    faithfulness,
    context_precision,
    context_recall,
    answer_relevancy
)

from ragas.llms import LangchainLLMWrapper
from langchain_openai import OpenAIEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from ragas.run_config import RunConfig

# ===============================
# IMPORT SISTEM RAG
# ===============================

from src.rag.generator import generate_answer
from src.retrieve.hybrid_retriever import hybrid_retrieve


# ===============================
# SETUP LLM EVALUATOR
# ===============================

evaluator_llm = LangchainLLMWrapper(
    ChatOpenAI(
        model="openai/gpt-4o-mini",
        temperature=0,
        openai_api_key=OPENAI_API_KEY,
        openai_api_base="https://api.maiarouter.ai/v1"
    )
)

evaluator_embeddings = LangchainEmbeddingsWrapper(
    OpenAIEmbeddings(
        model="openai/text-embedding-3-small",
        openai_api_key=EMBEDDING_API_KEY,
        openai_api_base="https://api.maiarouter.ai/v1"
    )
)


def convert_numpy(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.generic):
        return obj.item()
    return obj

# ===============================
# RUN EVALUATION
# ===============================

def run_evaluation():

    print("\nMemuat dataset evaluasi...\n")

    with open("data/eval/eval_questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    results = []

    total = len(questions)

    for i, q in enumerate(questions):

        question = q["question"]
        ground_truth = q["ground_truth"]

        print(f"\nEvaluasi {i+1}/{total}")
        print("Pertanyaan:", question)

        # ===============================
        # RETRIEVAL
        # ===============================

        retrieved_chunks = hybrid_retrieve(question, k=5)

        contexts = []

        for chunk in retrieved_chunks:

            if isinstance(chunk, dict):
                contexts.append(chunk.get("text", ""))

            else:
                contexts.append(str(chunk))

        # ===============================
        # GENERATE ANSWER
        # ===============================

        answer = generate_answer(question)

        print("Jawaban AI:", answer)

        # ===============================
        # SIMPAN HASIL
        # ===============================

        results.append({
            "question": question,
            "answer": answer,
            "contexts": contexts,
            "ground_truth": ground_truth
        })

    # ===============================
    # BUAT DATASET
    # ===============================

    dataset = Dataset.from_list(results)

    print("\nMemulai evaluasi RAGAS...\n")

    run_config = RunConfig(max_workers=1)

    score = evaluate(
        dataset,
        metrics=[
            context_precision,
            context_recall,
            faithfulness,
            answer_relevancy
        ],
        llm=evaluator_llm,
        embeddings=evaluator_embeddings,
        run_config=run_config
    )

# ===============================
# TAMPILKAN HASIL PER PERTANYAAN
# ===============================

    print("\n===== HASIL EVALUASI PER PERTANYAAN =====\n")

    df = score.to_pandas()

    print(df)

# ===============================
# HITUNG RATA-RATA METRIC
# ===============================

    avg_context_precision = df["context_precision"].mean()
    avg_context_recall = df["context_recall"].mean()
    avg_faithfulness = df["faithfulness"].mean()
    avg_answer_relevancy = df["answer_relevancy"].mean()

    print("\n===== RATA-RATA METRIC =====\n")

    print("Context Precision :", avg_context_precision)
    print("Context Recall :", avg_context_recall)
    print("Faithfulness :", avg_faithfulness)
    print("Answer Relevancy :", avg_answer_relevancy)

# ===============================
# FORMAT DATA UNTUK DISIMPAN
# ===============================

    evaluation_result = {
        "total_questions": len(df),

        "average_metrics": {
            "context_precision": float(avg_context_precision),
            "context_recall": float(avg_context_recall),
            "faithfulness": float(avg_faithfulness),
            "answer_relevancy": float(avg_answer_relevancy)
        },

        "detailed_results": [
            {k: convert_numpy(v) for k, v in row.items()}
            for row in df.to_dict(orient="records")
        ]
    }

# ===============================
# SIMPAN HASIL
# ===============================

    os.makedirs("data/eval/result", exist_ok=True)

    with open("data/eval/result/evaluation_result.json", "w", encoding="utf-8") as f:
        json.dump(evaluation_result, f, indent=4)

    print("\nHasil evaluasi disimpan di:")
    print("data/eval/result/evaluation_result.json\n")


# ===============================
# MAIN
# ===============================

if __name__ == "__main__":
    run_evaluation()