from fastapi import FastAPI
from routers.auth import router as auth_router
from routers.documents import router as documents_router
from routers.rag import router as rag_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(documents_router)
app.include_router(rag_router)

@app.get("/")
def home():
    return {"message": "Financial Document API running"}