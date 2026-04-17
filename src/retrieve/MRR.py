from src.retrieve.hybrid_retriever import hybrid_retrieve

# List 24 pertanyaan
queries = [
    # fakultas&prodi
    "Apa saja program studi yang tersedia di Fakultas Teknik Universitas Islam Riau?",
    "Program studi apa yang dimiliki Fakultas Agama Islam UIR pada jenjang S1?",
    "Apa saja program studi yang ditawarkan di Fakultas Ekonomi dan Bisnis UIR?",

    # beasiswa
    "Apa saja program beasiswa yang berasal dari Pemerintah Provinsi Riau?",
    "Apa program beasiswa yang disediakan oleh Pemerintah Kabupaten Siak?",
    "Apa saja beasiswa internal yang tersedia di Universitas Islam Riau?",

    # kalender akademik
    "Kapan pelaksanaan usulan dosen pengampu mata kuliah untuk semester ganjil 2025/2026?",
    "Kapan kegiatan input pengampu mata kuliah oleh program studi dilaksanakan?",
    "Kapan verifikasi pengampu mata kuliah oleh DLMA dilakukan pada semester ganjil?",

    # layanan akademik
    "Bagaimana prosedur pengisian KRS bagi mahasiswa?",
    "Apa saja syarat sebelum mahasiswa dapat mengisi KRS?",
    "Bagaimana cara mendapatkan informasi layanan beasiswa di UIR?",

    # KP
    "Bagaimana penentuan dosen pembimbing kerja praktek?",
    "Apa saja tugas dosen pembimbing dalam kerja praktek?",
    "Apa saja tahapan pelaksanaan kerja praktek?",

    # TA
    "Bagaimana proses sidang tugas akhir di UIR?",
    "Siapa saja tim penguji sidang tugas akhir?",
    "Berapa batas waktu perbaikan laporan tugas akhir?",

    # pedoman akademik
    "Apa saja komponen penilaian sidang tugas akhir?",
    "Apa kewajiban dosen sebelum perkuliahan?",
    "Apa tindakan pengawas saat terjadi pelanggaran ujian?",

    # pembayaran
    "Kapan pembayaran SPP tahap 1 semester ganjil 2025/2026?",
    "Kapan pembayaran SKS tahap 2 semester ganjil?",
    "Apa konsekuensi jika belum bayar UKT sebelum KRS?"
]

print("\nHASIL HYBRID RETRIEVAL (untuk MRR):\n")

for i, query in enumerate(queries, 1):
    print(f"\n==============================")
    print(f"QUERY {i}: {query}")
    print(f"==============================")

    results = hybrid_retrieve(query)

    for r in results:
        print("-", r)