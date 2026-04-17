import ollama

def rewrite_query(query):

    prompt = f"""
Perbaiki pertanyaan mahasiswa menjadi bahasa Indonesia formal.
Jangan mengubah makna pertanyaan.

PENTING:
- Jangan mengubah nama institusi (contoh: UIR, Universitas Islam Riau)
- Jangan mengganti nama menjadi institusi lain

Contoh:
apa aja sih syarat ngambil TA
→ apa syarat mengambil tugas akhir

kapan uts
→ kapan ujian tengah semester

Pertanyaan:
{query}

Jawaban:
"""

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0}
    )

    result = response["message"]["content"].strip()

    # ambil hanya baris pertama
    result = result.split("\n")[0]

    # bersihkan kata yang tidak perlu
    result = result.replace("Output:", "")
    result = result.replace("Jawaban:", "")
    result = result.replace('"', "")

    return result.strip()