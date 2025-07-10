from utils.file_loader import load_file
from utils.text_splitter import chunk_text
from utils.embedding import embed_chunks, store_in_faiss

def ingest_documents(file_paths):
    for path in file_paths:
        raw_text = load_file(path)
        chunks = chunk_text(raw_text)
        print("Generating embeddings...")
        vectors = embed_chunks(chunks)
        print("Saving FAISS index...")
        store_in_faiss(vectors, chunks)
