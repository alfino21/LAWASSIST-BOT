from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# Importing service functions from services modulefrom services.legal_advice import legal_advice
from services.summary_generator import summarize_legal_case
from services.legal_advice import legal_advice
from services.document_generator import generate_document  # ✅ Added

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
