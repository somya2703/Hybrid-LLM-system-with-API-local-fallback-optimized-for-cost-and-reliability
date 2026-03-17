from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.rag_pipeline import generate_answer
from backend.deps import get_vectorstore   

router = APIRouter()


class Question(BaseModel):
    question: str


@router.post("/ask")
def ask(q: Question, vectorstore=Depends(get_vectorstore)):
    result = generate_answer(q.question, vectorstore)
    return result