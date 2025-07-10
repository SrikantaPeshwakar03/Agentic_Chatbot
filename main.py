import uuid
from mcp.context_manager import ContextManager
from agents.retrieval_agent import retrieve_agent
from agents.llmresponse_agent import llm_response_agent
from agents.source_agent import source_attribution_agent
from agents.memory_agent import memory_agent
#integrates all the Agents

def run_agent_pipeline(user_query: str):
    ctx = ContextManager()
    trace_id = str(uuid.uuid4())

    retrieval_msg = retrieve_agent(user_query, trace_id)
    ctx.send(retrieval_msg)

    llm_msg = llm_response_agent(retrieval_msg)
    ctx.send(llm_msg)

    source_msg = source_attribution_agent(llm_msg)
    ctx.send(source_msg)

    final_msg = memory_agent(source_msg)
    ctx.send(final_msg)

    return ctx.get_trace(trace_id)

if __name__ == "__main__":
    query = input("Enter your question: ")
    trace = run_agent_pipeline(query)

    print("\n=== Agent Trace ===")
    for msg in trace:
        print(f"{msg['type']} from {msg['sender']} to {msg['receiver']}:\n{msg['payload']}\n")
