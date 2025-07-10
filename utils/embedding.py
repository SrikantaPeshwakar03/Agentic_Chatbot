from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")
index_file = "vector_store/faiss_index.pkl"

def embed_chunks(chunks):
    return model.encode(chunks)

def store_in_faiss(vectors, chunks):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)  # create a fresh index
    index.add(vectors)

    os.makedirs(os.path.dirname(index_file), exist_ok=True)
    with open(index_file, "wb") as f:
        pickle.dump((index, chunks), f)  # store only the new chunks
