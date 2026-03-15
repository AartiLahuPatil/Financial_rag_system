from fastapi import APIRouter, UploadFile, File
import shutil
import os
from PyPDF2 import PdfReader

from utils.chunking import chunk_text
from utils.embeddings import embed_text
from rag import add_document

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_FOLDER = "documents"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # read pdf
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    # chunk text
    chunks = chunk_text(text)

    # create embeddings + store in FAISS
    for chunk in chunks:
        embedding = embed_text(chunk)
        add_document(embedding, chunk)
        print("Chunk stored in FAISS")

    return {
        "message": "Document uploaded and processed",
        "chunks_added": len(chunks),
        "filename": file.filename
    }