from functools import lru_cache
from sklearn.feature_extraction.text import TfidfVectorizer
from text_search.document_builder import build_documents

@lru_cache(maxsize=1)
def build_index():
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(build_documents())

    return vectorizer, matrix
