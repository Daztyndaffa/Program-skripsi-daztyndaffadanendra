from spellchecker import SpellChecker

spell = SpellChecker(language=None)

# tambahkan kata domain kampus supaya tidak dianggap typo
spell.word_frequency.load_words([
    "ukt", "krs", "skripsi", "ta", "uts", "uas",
    "prodi", "npm", "kampus"
])

def correct_typo(text):

    words = text.split()

    corrected_words = []

    for word in words:
        corrected = spell.correction(word)
        corrected_words.append(corrected if corrected else word)

    return " ".join(corrected_words)