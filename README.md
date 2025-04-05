# 🧠 SHL Assessment Recommender

The SHL Assessment Recommender is an intelligent system designed to suggest the most relevant SHL assessments for a given job description (JD) or natural language query. It leverages sentence embeddings and the Gemini LLM to extract key information and return precise recommendations, enhancing the hiring process and ensuring alignment between job requirements and cognitive/personality testing.

---

## 🔍 Features

- 🔗 **JD URL Scraping**: Paste a link to a job description, and the system will automatically fetch and use its content.
- 🧠 **LLM-Powered Skill Extraction**: Uses Google Gemini to extract skills, roles, and levels from the input query or JD.
- 💡 **Smart Embedding Search**: Uses `sentence-transformers` (`all-MiniLM-L6-v2`) to embed both JD and assessment descriptions for similarity search.
- 📋 **SHL Test Database Matching**: Finds and ranks top SHL assessments based on relevance to the input query.
- 📊 **Similarity Scoring**: Displays a similarity score with each result to help prioritize options.
- 🌐 **FastAPI Backend**: An API-first design allows this logic to be reused in other products.
- 🧪 **Streamlit Frontend**: Interactive, responsive UI for experimentation and quick results.

---

## ⚙️ Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: FastAPI
- **LLM**: Google Gemini API (for intent and skill extraction)
- **Embeddings**: `sentence-transformers` (MiniLM)
- **Scraping**: `requests` + `BeautifulSoup`
- **Data**: `shl_data.json` containing assessment descriptions and metadata

## 📦 shl-assessment-recommender/
```
├── app.py                # Streamlit UI
├── main.py               # FastAPI backend
├── suggest.py            # Core logic for suggesting assessments
├── data_loader.py        # Load and embed SHL data
├── model_loader.py       # SentenceTransformer model loader
├── shl_data.json         # Assessment data
├── .env                  # Environment variables (not committed)
├── .gitignore            # Git ignored files/folders
└── requirements.txt      # Python dependencies
```