from functools import lru_cache
from sklearn.feature_extraction.text import TfidfVectorizer
from text_search.document_builder import build_documents

@lru_cache(maxsize=1)
def build_index():
    documents = build_documents()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    return vectorizer, tfidf_matrix
