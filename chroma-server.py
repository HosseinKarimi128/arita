from fastapi import FastAPI, HTTPException, Depends, status, Response
from pydantic import BaseModel
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from typing import Optional
from uuid import uuid4
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from dotenv import load_dotenv
import os

load_dotenv()

CHROMA_PATH = "./chroma"
OPENAI_TOKEN = os.getenv("OPENAI_API_KEY")
VALID_TOKEN = os.getenv("CHROMA_ACCESS_TOKEN")
EMBEDDINGS = OpenAIEmbeddings(api_key=OPENAI_TOKEN)


app = FastAPI(
  title="Chroma Server",
  version="1.0",
  description="""A simple API server serving queries on a Chroma vector store.""",
)
auth_scheme = HTTPBearer()



def authenticate(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    """
    Authentication dependency that validates the provided token.
    """
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials


def format_metadata(metadata: dict):

    # Mapping of input keys to desired keys in the output
    key_mapping = {
        "tools": "tools",
        "type": "type",
        "kw": "kw"
    }
    
    # Build the `$and` list
    conditions = [
        {key_mapping[key]: {"$eq": value}}
        for key, value in metadata.items() if key in key_mapping
    ]
    
    return {"$and": conditions} if conditions else {}



def query_rag(query_text: str, k: int, maximum_distance: float, metadata: dict):

    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=EMBEDDINGS)
    
    if metadata is None:
        results = db.similarity_search_with_score(query=query_text,k=k)
    elif len(metadata) == 1:
        results = db.similarity_search_with_score(query=query_text,
                                                filter=metadata,
                                                k=k
                                                )
    else:
        filters = format_metadata(metadata)   # since Chroma has issues with multiple values for filter 
        results = db.similarity_search_with_score(query=query_text,
                                                filter=filters,
                                                k=k
                                                )
        
    new_results = [i for i in results if i[1] < maximum_distance] 
    
    if len(new_results) == 0:
        raise HTTPException(status_code=500, detail="Unable to find matching results")

    return new_results




def save_to_chroma_texts(chunks: list[str], metadatas: list[dict]):

    ids = [str(uuid4()) for _ in range(len(chunks))]
    docs = [Document(page_content=i, metadata=j) for i,j in zip(chunks, metadatas)]

    try:
        db = Chroma.from_documents(
            documents=docs,
            embedding=EMBEDDINGS,
            ids=ids,
            persist_directory=CHROMA_PATH,
        )
        return Response(content=f"Saved {len(chunks)} chunks to {CHROMA_PATH}.",
                        status_code=200)
    
    except Exception:
        raise HTTPException(status_code=500, detail=Exception)
  



class InsertRequestText(BaseModel):
    facts: list[str]                             # Contains the facts (generated from feedback)
    metadatas: Optional[list[dict]] = None       # IDs for each record in DB

class RetrieveRequest(BaseModel):
    query: str                                   # The input query
    metadata: Optional[dict] = None              # For filtering 
    k: Optional[int] = 1                         # The number of retrieved results
    maximum_distance: Optional[float] = 0.4      # The maximum similarity distance



@app.post("/insert-texts")
async def insert(request: InsertRequestText, auth: HTTPAuthorizationCredentials = Depends(authenticate)):
    if not request.facts:
        raise HTTPException(status_code=400, detail="Facts cannot be empty")
    
    response = save_to_chroma_texts(request.facts, request.metadatas)

    return response


@app.post("/retrieve")
async def retrieve(request: RetrieveRequest, auth: HTTPAuthorizationCredentials = Depends(authenticate)):
    if not request.query:
        raise HTTPException(status_code=400, detail="query cannot be empty")
    if request.k < 1 or type(request.k) != int:
        raise HTTPException(status_code=400, detail="k (number of results) must be at least 1")
    if request.maximum_distance > 1 or request.maximum_distance < 0:
        raise HTTPException(status_code=400, detail="maximum_distance must be range (0,1)")
    
    response = query_rag(request.query, request.k, request.maximum_distance, request.metadata)
    
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8324)
