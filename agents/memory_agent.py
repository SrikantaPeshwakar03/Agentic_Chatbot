from mcp.context_manager import Message

memory_store = []

def memory_agent(source_msg: Message) -> Message:
    memory_store.append({
        "trace_id": source_msg.trace_id,
        "query": source_msg.payload["query"],
        "response": source_msg.payload["final_answer"][:1000]
    })

    return Message(
        sender="MemoryAgent",
        receiver="User",
        msg_type="FINAL_RESPONSE",
        trace_id=source_msg.trace_id,
        payload={
            "response": source_msg.payload["final_answer"]
        }
    )
