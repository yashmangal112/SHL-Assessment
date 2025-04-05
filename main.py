import os
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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # fallback to 8000 if PORT not set
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)