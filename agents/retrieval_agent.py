import faiss
import pickle
from sentence_transformers import SentenceTransformer
from mcp.context_manager import Message

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_vector_store(path="vector_store/faiss_index.pkl"):
    with open(path, "rb") as f:
        index, texts = pickle.load(f)
    return index, texts

def retrieve_agent(query: str, trace_id: str):
    index, texts = load_vector_store()
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k=2)
    top_chunks = [texts[i][:1000] for i in indices[0]]

    return Message(
        sender="RetrievalAgent",
        receiver="LLMResponseAgent",
        msg_type="CONTEXT_RESPONSE",
        trace_id=trace_id,
        payload={
            "query": query,
            "top_chunks": top_chunks
        }
    )
