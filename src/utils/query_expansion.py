def expand_query(query):

    query = query.lower()

    # pertanyaan waktu
    if "kapan" in query:
        query += " jadwal tanggal periode waktu pelaksanaan"

    # pertanyaan syarat
    if "syarat" in query:
        query += " persyaratan ketentuan"

    # pertanyaan cara
    if "cara" in query or "bagaimana" in query:
        query += " prosedur langkah"

    return query