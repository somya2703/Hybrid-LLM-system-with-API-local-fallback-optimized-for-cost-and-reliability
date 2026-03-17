# Training Knowledge Assistant (RAG + Fallback LLM)

A production-style **Retrieval-Augmented Generation (RAG)** system that answers questions from custom documents using:

*  **OpenAI (primary LLM)** for high-quality responses
*  **Local LLM (TinyLlama via llama.cpp)** as a fallback when API quota is unavailable
*  Fully containerized with Docker
*  CPU friendly deployment

---

#  Key Features

*  RAG pipeline using **FAISS vector database**
*  OpenAI-powered responses (primary)
*  Automatic fallback to **local LLM (TinyLlama GGUF)**
*  Works even with **zero API credits**
*  Streamlit chat interface
*  FastAPI backend (production ready structure)
*  Dockerized multi-service architecture
*  Automatic vector DB creation on startup

---

#  Architecture

```
User (Streamlit UI)
        ↓
FastAPI Backend (/ask)
        ↓
Retriever (FAISS)
        ↓
LLM Decision Layer
   ├── OpenAI (primary)
   └── Local LLM (fallback via llama.cpp)
```

---

#  Tech Stack

### Backend

* FastAPI
* LangChain
* FAISS (Vector DB)

### LLMs

* OpenAI API (primary)
* TinyLlama (GGUF, via llama.cpp)

### Frontend

* Streamlit

### Infra / DevOps

* Docker & Docker Compose
* Makefile automation

---

# ⚙️ How It Works

1. Documents (PDFs) are chunked and embedded using sentence-transformers
2. Stored in FAISS vector database
3. On query:

   * Relevant chunks are retrieved
   * Sent to LLM for answer generation
4. System tries:

   *  OpenAI first
   *  Falls back to local LLM if:

     * API quota exceeded
     * API unavailable

---

#  Running the Project

## Option 1 — Docker (Recommended)

### 1. Build

```bash
make build
```

### 2. Run

```bash
make up
```

---

### Access apps:

*  Backend API Docs: http://localhost:8000/docs
*  Streamlit UI: http://localhost:8501

---

##  Option 2 — Local Run

### Backend

```bash
uvicorn backend.main:app --reload
```

### Frontend

```bash
streamlit run app/streamlit_app.py
```

---

#  Data Setup

Place your PDFs in (you can also use the dummy file generator in /scripts to generate files for testing purpose):

```
dummy_data/
```

Vector DB is automatically created on startup.

---

#  Local LLM Setup

1. Download GGUF model (e.g., TinyLlama)
2. Place inside:

```
models/
```

Example:

```
models/tinyllama.gguf
```

---

#  Fallback Behavior

| Scenario         | Model Used   |
| ---------------- | ------------ |
| OpenAI available |  OpenAI     |
| No API quota     |  Local LLM |
| No internet      |  Local LLM |

---

This system can be adapted for:

*  Internal company knowledge assistants
*  Factory documentation querying
*  Robotics troubleshooting assistants
*  Engineering knowledge retrieval systems
*  Training & onboarding copilots

---

This project demonstrates:

* End-to-end ML system design
* LLM integration with fallback strategies
* Production ready backend architecture
* Containerized deployment
* Cost aware AI system design (API + local hybrid)

---

