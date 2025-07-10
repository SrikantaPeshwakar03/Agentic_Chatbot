from mcp.context_manager import Message

def source_attribution_agent(llm_msg: Message) -> Message:
    query = llm_msg.payload["query"]
    answer = llm_msg.payload.get("answer", "").strip()
    sources = llm_msg.payload.get("top_chunks", [])

    # ✅ Limit number of sources and truncate long texts
    max_sources = 2
    max_source_length = 500  # characters

    trimmed_sources = [src[:max_source_length] for src in sources[:max_sources]]
    
    if not answer:
        final_answer = "❌ Failed to generate an answer. Please check logs or model status."
    else:
        source_text = "\n---\n".join(trimmed_sources)
        final_answer = f"{answer}\n\n🗂️ **Sources**:\n{source_text}"

    return Message(
        sender="SourceAttributionAgent",
        receiver="MemoryAgent",
        msg_type="ANSWER_WITH_SOURCES",
        trace_id=llm_msg.trace_id,
        payload={
            "query": query,
            "final_answer": final_answer
        }
    )
