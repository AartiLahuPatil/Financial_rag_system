from fastapi import APIRouter
from pydantic import BaseModel
from utils.embeddings import embed_text
from rag import search

router = APIRouter(
    prefix="/rag",
    tags=["RAG Search"]
)

class QueryRequest(BaseModel):
    query: str


@router.post("/search")
def search_documents(request: QueryRequest):

    query_embedding = embed_text(request.query)

    results = search(query_embedding)

    return {
        "query": request.query,
        "results": results
    }