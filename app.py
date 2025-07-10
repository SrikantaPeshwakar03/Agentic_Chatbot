import gradio as gr
from agents.ingestion_agent import ingest_documents
from main import run_agent_pipeline
from config import MODEL_NAME
# this function is used to take question from the user
def ask_question(query, files):
    if files:
        file_paths = [f.name for f in files]
        ingest_documents(file_paths)

    trace = run_agent_pipeline(query)
    final_msg = next((m for m in trace if m["type"] == "FINAL_RESPONSE"), None)

    if final_msg:
        answer = final_msg["payload"]["response"]
    else:
        answer = "Failed to generate an answer. Please check logs or model status."

    return answer, ""

def user_chat_handler(chat_history, message, files):
    answer, _ = ask_question(message, files)
    chat_history = chat_history + [(message, answer)]
    return chat_history, "", files

def show_uploaded_files(files):
    if not files:
        return ""
    return "\n".join([f.name for f in files])

with gr.Blocks(css="style.css") as demo:
    gr.Markdown("# 🤖 Agentic RAG Chatbot with LLaMA 3.2")
    gr.Markdown(f"🦙 **Model**: `{MODEL_NAME}`")

    chatbot = gr.Chatbot(label="Chat History", height=400)

    with gr.Row(elem_id="bottom-row"):
        with gr.Column(scale=0.5):
            file_upload = gr.File(
                file_types=[".pdf", ".csv", ".pptx", ".docx", ".txt", ".md"],
                file_count="multiple",
                label="📎",
                elem_id="upload-btn"
            )
            file_list_display = gr.Markdown(value="", elem_id="file-names")

        with gr.Column(scale=3):
            msg_input = gr.Textbox(placeholder="Ask your question...", lines=1, interactive=True, elem_id="msg-box")

        with gr.Column(scale=0.5):
            submit_btn = gr.Button("Submit", elem_id="submit-btn")

    msg_input.submit(fn=user_chat_handler, inputs=[chatbot, msg_input, file_upload], outputs=[chatbot, msg_input, file_upload])
    submit_btn.click(fn=user_chat_handler, inputs=[chatbot, msg_input, file_upload], outputs=[chatbot, msg_input, file_upload])
    file_upload.change(fn=show_uploaded_files, inputs=file_upload, outputs=file_list_display)

    gr.Markdown("Powered by Ollama + Agentic RAG")

if __name__ == "__main__":
    demo.launch()
