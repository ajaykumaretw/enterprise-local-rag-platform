# Enterprise Local RAG Platform

A modern AI-powered Retrieval-Augmented Generation (RAG) platform built using Flask, RequireJS, LangChain LCEL, ChromaDB, Ollama, and local Large Language Models (LLMs).

---

# 🚀 Features

- PDF Upload & Processing
- AI Question Answering
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Local LLM Integration using Ollama
- ChromaDB Vector Database
- RequireJS Modular Frontend
- Flask REST APIs
- Fully Local AI Stack
- Modern LCEL-based LangChain Pipelines

---

# 🏗️ System Architecture

```plaintext
Frontend (RequireJS)
        ↓
Flask APIs
        ↓
LangChain LCEL Pipeline
        ↓
ChromaDB Vector Store
        ↓
Ollama Embeddings
        ↓
Gemma3 LLM
```

---

# 🛠️ Tech Stack

## Backend

- Flask
- Python
- LangChain
- ChromaDB
- Ollama

## Frontend

- RequireJS
- JavaScript
- HTML5
- CSS3

## AI / ML

- Retrieval-Augmented Generation (RAG)
- LCEL
- Vector Embeddings
- Semantic Search
- Gemma3
- Nomic Embeddings

---

# 📂 Project Structure

```plaintext
enterprise-local-rag-platform/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── chroma_db/
│
├── uploads/
│
├── templates/
│   └── index.html
│
├── static_js/
│   ├── api.js
│   ├── app.js
│   ├── main.js
│   ├── math.js
│   ├── message.js
│   ├── rag.js
│   │
│   └── lib/
│       └── require.min.js
│
└── venv/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/ajaykumaretw/enterprise-local-rag-platform.git
```

---

## 2. Navigate to Project

```bash
cd enterprise-local-rag-platform
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download Ollama:

https://ollama.com/

---

# 📥 Pull Required Models

## Pull Gemma3

```bash
ollama pull gemma3
```

## Pull Embedding Model

```bash
ollama pull nomic-embed-text
```

---

# ▶️ Start Ollama

```bash
ollama serve
```

---

# ▶️ Run Flask Application

```bash
python app.py
```

---

# 🌐 Open Application

```plaintext
http://127.0.0.1:5000
```

---

# 📄 Application Workflow

## Upload PDF

1. Select PDF file
2. Click Upload PDF
3. PDF is chunked and embedded
4. Data stored inside ChromaDB

---

## Ask Questions

1. Enter question
2. Click Ask AI
3. Relevant chunks retrieved
4. Gemma3 generates contextual response

---

# 🧠 RAG Pipeline

```plaintext
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Retriever
 ↓
Gemma3
 ↓
AI Response
```

---

# 📸 Features Included

- Upload PDF
- Ask Questions From PDF
- AI Response Panel
- RequireJS Modular Frontend
- Flask APIs
- Local AI Processing
- Semantic Search
- Vector Retrieval

---

# 🚀 Future Enhancements

- Multi-PDF Support
- Authentication System
- Chat History
- Streaming AI Responses
- Docker Deployment
- Kubernetes Deployment
- Voice Input
- Multi-Agent Workflows
- Real-Time Analytics Dashboard

---

# 💼 Resume Highlights

- Developed enterprise-grade RAG architecture
- Built semantic retrieval pipelines
- Integrated Ollama local LLM workflows
- Designed modular frontend using RequireJS
- Developed scalable Flask REST APIs
- Implemented ChromaDB vector search
- Created LCEL-based LangChain pipelines

---

# 📚 Concepts Used

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embeddings
- Semantic Search
- Local LLMs
- LangChain LCEL
- Async API Communication

---

# 🌟 Key Highlights

- Fully Local AI Stack
- Enterprise RAG Architecture
- Vector Similarity Search
- Modular Frontend Design
- Local LLM Integration
- Semantic Retrieval Pipelines

---

# 👨‍💻 Author

Ajay Kumar

Senior Python Developer

---

# ⭐ Support

If you like this project, give it a star on GitHub ⭐