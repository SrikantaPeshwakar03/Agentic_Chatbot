import requests
from mcp.context_manager import Message
from config import OLLAMA_API_URL, MODEL_NAME

def llm_response_agent(context_message: Message) -> Message:
    payload = context_message.payload
    query = payload["query"]
    chunks = payload["top_chunks"]

    context_text = "\n\n".join(chunks)
    prompt = f"Context:\n{context_text}\n\nQuestion:\n{query}\nAnswer:"


    response = requests.post(OLLAMA_API_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    if response.status_code != 200:
        print("LLM generation failed:", response.text)
        return Message(
            sender="LLMResponseAgent",
            receiver="SourceAttributionAgent",
            msg_type="ANSWER_GENERATED",
            trace_id=context_message.trace_id,
            payload={
                "query": query,
                "answer": None,
                "top_chunks": chunks
            }
        )

    answer = response.json().get('response', '').strip()

    return Message(
        sender="LLMResponseAgent",
        receiver="SourceAttributionAgent",
        msg_type="ANSWER_GENERATED",
        trace_id=context_message.trace_id,
        payload={
            "query": query,
            "answer": answer,
            "top_chunks": chunks
        }
    )
