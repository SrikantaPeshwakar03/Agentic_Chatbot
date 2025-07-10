# 🤖 Agentic RAG Chatbot with LLaMA 3.2

This is an **Agent-based Retrieval-Augmented Generation (RAG)** chatbot powered by **Meta’s LLaMA 3.2** running via **Ollama**. It supports document ingestion and natural language question answering using modular agents and FAISS for vector search using Model Context Protocol.

---

## Features

- Agentic pipeline: Retrieval → LLM → Source Attribution → Memory
- Multi-format document ingestion: PDF, CSV, PPTX, DOCX, TXT, MD
- FAISS-powered semantic retrieval using Sentence Transformers
- LLaMA 3.2 via [Ollama](https://ollama.com/)
- Clean UI via Gradio

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SrikantaPeshwakar03/Agentic_Chatbot.git
cd agentic-chatbot
```
## 2. Create & Activate Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate         # On Linux/Mac
venv\Scripts\activate            # On Windows
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## 4. Download Ollama
- Download Ollama from https://ollama.com/download
- After Downloading, open Command Prompt and run:
```bash
ollama run llama3.2
```
- Make sure the llama3.2 is running locally while you run the Chatbot

## 5. Running the App

Once dependencies are installed and Ollama is set up, you can run the chatbot using:

```bash
python app.py
```
