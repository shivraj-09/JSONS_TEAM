from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.agent import process_customer_query


app = FastAPI(
    title="AI Customer Support Agent",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CustomerQuery(BaseModel):
    query: str


@app.get("/")
def root():
    return {
        "message": "AI Customer Support Agent is running"
    }


@app.post("/support")
def support(request: CustomerQuery):

    if not request.query.strip():
        return {
            "error": "Customer query cannot be empty"
        }

    return process_customer_query(request.query)