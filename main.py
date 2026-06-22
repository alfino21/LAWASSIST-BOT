from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import UploadFile, File
import os

# Importing service functions from services modulefrom services.legal_advice import legal_advice
# Importing service functions
from services.legal_advice import legal_advice
from services.summary_generator import summarize_legal_case
from services.document_generator import generate_document
from services.pdf_service import extract_text_from_pdf
from services.legal_analyzer import analyze_legal_document
from services.pdf_report import generate_analysis_pdf
from services.rag.rag_service import (
    legal_rag_query
)
from pydantic import BaseModel
class ChatRequest(BaseModel):
    message: str
app = FastAPI()

# Enable CORS so frontend JavaScript can access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from the frontend folder
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Serve index.html at the root route
@app.get("/")
async def read_index():
    index_path = os.path.join("frontend", "index.html")
    return FileResponse(index_path)

# ---------------- API Endpoints ---------------- #

@app.post("/generate-document/")
async def doc_gen(request: Request):
    data = await request.json()
    doc_type = data.get("type")
    details = data.get("details", {})
    return {"document": generate_document(doc_type, details)}

@app.post("/legal-advice/")
async def legal_help(request: Request):
    data = await request.json()
    question = data.get("question")
    return {"advice": legal_advice(question)}

@app.post("/summarize/")
async def summary(request: Request):
    data = await request.json()
    text = data.get("text")
    return {"summary": summarize_legal_case(text)}

@app.post("/analyze-pdf")
async def analyze_pdf(file: UploadFile = File(...)):

    upload_path = f"uploads/{file.filename}"

    os.makedirs("uploads", exist_ok=True)

    with open(upload_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(upload_path)

    analysis = analyze_legal_document(text)

    return {
        "filename": file.filename,
        "analysis": analysis
    }
    
@app.post("/download-analysis")
async def download_analysis(request: Request):

    data = await request.json()

    report = data.get("report", "")

    filename = "analysis_report.pdf"

    generate_analysis_pdf(
        report,
        filename
    )

    return FileResponse(
        path=filename,
        media_type="application/pdf",
        filename="analysis_report.pdf"
    )
@app.post("/legal-search")
async def legal_search(request: Request):

    data = await request.json()

    question = data.get("question")

    answer = legal_rag_query(question)

    return {
        "answer": answer
    }
@app.post("/chat")
async def chat(request: ChatRequest):
    message = request.message
    
    if "article" in message.lower() or "section" in message.lower():
        response = legal_rag_query(message)
    else:
        response = legal_advice(message)
    
    return {"response": response}