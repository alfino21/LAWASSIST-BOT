# ⚖️ LawAssistBot

An AI-powered Legal Assistant built using FastAPI, RAG (Retrieval-Augmented Generation), Vector Databases, and Large Language Models to help users understand legal documents, generate legal drafts, summarize cases, and retrieve information from Indian legal resources.

---

## 🚀 Features

### 📄 Legal Document Generator
Generate common legal documents such as:
- Rental Agreements
- Non-Disclosure Agreements (NDA)
- Custom Legal Drafts

### 💡 Legal Advice Assistant
Ask legal questions and receive AI-powered legal guidance based on available legal knowledge.

### 🧾 Case Summarization
Summarize lengthy legal cases into concise and understandable summaries.

### 📑 Legal PDF Analyzer
Upload legal PDFs and get:
- Key clause extraction
- Legal risk analysis
- Important observations
- AI-generated insights

### 📥 PDF Report Generation
Download analysis reports in PDF format.

### 🔍 Legal Knowledge Search (RAG)
Search across:
- Constitution of India
- Bharatiya Nyaya Sanhita (BNS)
- Consumer Protection Act
- Other legal documents

Powered by:
- Hugging Face Embeddings
- ChromaDB Vector Database
- Retrieval-Augmented Generation (RAG)

---

## 🏗️ Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI & NLP
- OpenAI API
- LangChain
- Hugging Face Embeddings
- RAG Architecture

### Vector Database
- ChromaDB

### Frontend
- HTML
- CSS
- JavaScript

### PDF Processing
- PyPDF2
- ReportLab

---

## 📂 Project Structure

```text
LAWASSISTBOT/
│
├── frontend/
│   └── index.html
│
├── legal_docs/
│   ├── constitution.txt
│   ├── bns_sections.txt
│   └── consumer_protection.txt
│
├── services/
│   ├── legal_advice.py
│   ├── document_generator.py
│   ├── summary_generator.py
│   ├── legal_analyzer.py
│   ├── pdf_service.py
│   ├── pdf_report.py
│   │
│   └── rag/
│       ├── load_documents.py
│       ├── vector_store.py
│       ├── retriever.py
│       └── rag_service.py
│
├── uploads/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/lawassistbot.git
cd lawassistbot
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🧠 RAG Knowledge Base Setup

Load legal documents into ChromaDB:

```bash
python create_db.py
```

This will:
- Read legal documents
- Generate embeddings
- Store vectors in ChromaDB
- Enable semantic legal search

---

## 🎯 Future Enhancements

- Chatbot Popup Interface
- React Frontend
- Authentication System
- Legal Case Prediction
- Multilingual Support
- Indian Legal LLM Integration
- Citation-based Responses
- Cloud Deployment

---

## ⚠️ Disclaimer

LawAssistBot provides AI-generated legal information for educational and informational purposes only. It does not constitute professional legal advice. Always consult a qualified legal professional before making legal decisions.

---

## 👨‍💻 Developer

**Alfi (Alfino Christ B)**

B.Tech Artificial Intelligence & Data Science

Specializations:
- Generative AI
- Retrieval-Augmented Generation (RAG)
- AI Agents
- FastAPI Development
- Machine Learning

---

## 📜 License

This project is licensed under the MIT License.