# Financial Document Management System (RAG Based)

## Project Overview
This project is a Financial Document Retrieval System built using FastAPI and a Retrieval-Augmented Generation (RAG) approach.

It allows users to upload financial PDF documents and ask questions about them. The system processes the document, converts the text into embeddings, stores them in a vector database, and retrieves the most relevant information when a query is asked.

The main goal of the project is to quickly extract financial insights from large documents such as financial reports, risk reports, and analysis documents.

----------------------------------------------------

## Technologies Used

Python  
FastAPI (Backend API Framework)  
FAISS (Vector Search Engine)  
Sentence Transformers (Embedding Model)  
MySQL (User and metadata storage)  
PyPDF2 (PDF text extraction)

----------------------------------------------------

## Project Structure

financial_document_rag
│
├── main.py  
├── database.py  
├── models.py  
├── rag.py  
│
├── routers  
│     ├── auth.py  
│     ├── documents.py  
│     └── rag.py  
│
├── utils  
│     ├── embeddings.py  
│     └── chunking.py  
│
└── documents  

----------------------------------------------------

## How the System Works

1. User uploads a financial PDF document.
2. The system extracts text from the PDF.
3. The text is divided into smaller chunks.
4. Each chunk is converted into embeddings using a sentence transformer model.
5. Embeddings are stored in a FAISS vector index.
6. When the user asks a question, the query is converted into an embedding.
7. FAISS searches for the most similar document chunks.
8. The system returns the relevant information as the response.

----------------------------------------------------

## API Endpoints

Register User  
POST /auth/register  

Login User  
POST /auth/login  

Upload Financial Document  
POST /documents/upload  

Search Query in Documents  
POST /rag/search  

----------------------------------------------------

## Example Query Request

{
  "query": "What are the financial risks mentioned in the report?"
}

----------------------------------------------------

## Example Response

{
  "query": "What are the financial risks mentioned in the report?",
  "results": [
    "Liquidity risk occurs when a company cannot meet short-term obligations.",
    "Credit risk arises when borrowers fail to repay loans."
  ]
}

----------------------------------------------------

## Installation Steps

1. Install required libraries

pip install fastapi uvicorn sqlalchemy pymysql python-multipart sentence-transformers faiss-cpu PyPDF2

2. Start the FastAPI server

uvicorn main:app --reload

3. Open the API documentation

http://127.0.0.1:8000/docs

----------------------------------------------------

## Features

Upload financial documents  
Extract and process PDF content  
Convert text to embeddings  
Perform semantic search using FAISS  
Retrieve relevant financial insights quickly  

----------------------------------------------------

## Future Improvements

Integration with large language models for better answer generation  
Support for multiple document formats  
Advanced financial analytics and summarization  
Persistent vector database storage  

----------------------------------------------------

## Conclusion

This project demonstrates how Retrieval-Augmented Generation (RAG) can be used to efficiently retrieve information from large financial documents. It combines FastAPI for backend services, FAISS for vector search, and machine learning embeddings for semantic understanding.