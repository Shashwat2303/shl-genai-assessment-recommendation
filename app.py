from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI()

model = SentenceTransformer("all-MiniLM-L6-v2")

CATALOG = [
    {"name":"Java Programming","url":"https://www.shl.com/","description":"Java skills","test_type":["K"],"duration":40,"adaptive_support":"Yes","remote_support":"Yes"},
    {"name":"Teamwork","url":"https://www.shl.com/","description":"Collaboration skills","test_type":["P"],"duration":30,"adaptive_support":"No","remote_support":"Yes"}
]

embeddings = model.encode([c["description"] for c in CATALOG], normalize_embeddings=True)

class Query(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.post("/recommend")
def recommend(q: Query):
    q_emb = model.encode([q.query], normalize_embeddings=True)
    scores = np.dot(embeddings, q_emb.T).flatten()
    idx = scores.argsort()[::-1][:5]
    return {"recommended_assessments":[CATALOG[i] for i in idx]}
