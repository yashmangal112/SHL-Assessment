# suggest.py
import re
import requests
from bs4 import BeautifulSoup
from data_loader import df, MODEL
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-pro")

def extract_text_from_url(url: str) -> str:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text(separator="\n")
    except Exception as e:
        return f"Error scraping URL: {str(e)}"

def enrich_with_gemini(prompt_text: str) -> str:
    prompt = f"""
Extract the following fields from this job description or query:

- Key Skills
- Role
- Time Limit (if any)
- Level (e.g., analyst, executive, manager)

Return a list of bullet points, no explanation.

Job Description:
{prompt_text}
"""
    try:
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return ""

def suggest(query: str, top_k: int = 10):
    if re.match(r"https?://", query.strip()):
        query = extract_text_from_url(query)

    llm_enhancement = enrich_with_gemini(query)

    combined_query = f"{query.strip()}\n\nAdditional Info:\n{llm_enhancement.strip()}"

    query_emb = MODEL.encode(combined_query, convert_to_tensor=True)
    similarities = [
        cosine_similarity(query_emb.unsqueeze(0).cpu().numpy(), emb.unsqueeze(0).cpu().numpy())[0][0]
        for emb in df["embedding"]
    ]

    df["score"] = similarities
    results = df.sort_values("score", ascending=False).head(top_k)
    return results[[
        "Assessment Name",
        "URL",
        "Remote Testing",
        "Adaptive/IRT",
        "Duration",
        "Test Type",
        "Description",
        "score"
    ]].to_dict(orient="records")
