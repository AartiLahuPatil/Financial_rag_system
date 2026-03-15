import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

documents = []

def add_document(embedding, text):

    index.add(np.array([embedding]))
    documents.append(text)


def search(query_embedding):

    if len(documents) == 0:
        return ["No documents uploaded yet"]

    D, I = index.search(np.array([query_embedding]), 5)

    results = []

    for i in I[0]:
        if i < len(documents):
            results.append(documents[i])

    return results