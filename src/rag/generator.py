import ollama

from src.retrieve.hybrid_retriever import hybrid_retrieve
from src.config.settings import OLLAMA_HOST
from src.rag.query_rewriter import rewrite_query
from src.utils.query_expansion import expand_query
from src.utils.protect_terms import protect_terms
from src.utils.logger import save_chat

# ==========================================
# SYSTEM PROMPT
# ==========================================

SYSTEM_PROMPT = """
Kamu adalah AI Assistant Universitas Islam Riau.

Tugas kamu:
- HANYA menjawab berdasarkan konteks dokumen resmi UIR
- DILARANG menjawab di luar konteks

Aturan:
- Jika pertanyaan TIDAK berkaitan dengan Universitas Islam Riau → jawab:
  "Maaf, saya hanya dapat menjawab pertanyaan terkait Universitas Islam Riau."

- Jika informasi tidak ada di konteks → jawab:
  "Maaf, informasi tersebut tidak ditemukan dalam dokumen resmi Universitas Islam Riau."

- Jangan memberikan penjelasan tambahan di luar konteks
- Jawaban harus singkat dan langsung
"""


# ==========================================
# BUILD CONTEXT
# ==========================================

def build_context(chunks):
    return "\n\n".join(chunks)


# ==========================================
# GENERATE ANSWER
# ==========================================
def generate_answer(question):

    question = protect_terms(question)

    question = rewrite_query(question)

    question = expand_query(question)

    print("Query setelah diperbaiki:", question)

    chunks = hybrid_retrieve(question, k=5)

    if not chunks:
        answer = "Maaf, informasi tersebut tidak ditemukan dalam dokumen resmi Universitas Islam Riau."
        save_chat(question, answer)
        return answer

    context = build_context(chunks)

    prompt = f"""
{SYSTEM_PROMPT}

Konteks dokumen:
{context}

Pertanyaan mahasiswa:
{question}

Jawaban:
"""

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        options={
            "temperature": 0.2,
            "top_p": 0.9,
        }
    )

    answer = response["message"]["content"]

    if not answer.strip():
        answer = "Maaf, informasi tersebut tidak ditemukan dalam dokumen resmi Universitas Islam Riau."

    save_chat(question, answer)

    return answer