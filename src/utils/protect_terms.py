import re

def protect_terms(text):
    text = re.sub(r"\bUIR\b", "__UIR__", text, flags=re.IGNORECASE)
    text = re.sub(r"\bUniversitas Islam Riau\b", "__UIR_FULL__", text, flags=re.IGNORECASE)
    return text


def restore_terms(text):
    text = text.replace("__UIR__", "UIR")
    text = text.replace("__UIR_FULL__", "Universitas Islam Riau")
    return text