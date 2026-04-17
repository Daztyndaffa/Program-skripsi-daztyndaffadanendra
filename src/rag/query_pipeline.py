from src.utils.protect_terms import protect_terms, restore_terms
from src.rag.query_rewriter import rewrite_query
from src.utils.query_expansion import expand_query


def process_query(query):

    original_query = query

    # 1. protect terms
    query = protect_terms(query)

    # 2. rewrite
    query = rewrite_query(query)

    # 3. expand
    query = expand_query(query)

    # 4. restore terms
    query = restore_terms(query)

    return {
        "original": original_query,
        "processed": query
    }