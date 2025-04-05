# main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from suggest import suggest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/suggest")
def get_recommendations(query: str = Query(..., min_length=10)):
    return suggest(query)