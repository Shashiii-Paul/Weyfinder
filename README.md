# Weyfinder AI Career Navigator 🚀

**Weyfinder** is an AI-powered career guidance tool for people in New Zealand.  
It recommends careers, courses, workshops, certifications, and apprenticeships, considering practical constraints like commute and internet availability.

---

## Features

- Personalized career recommendations  
- Local and online courses/workshops  
- Actionable plans tailored to user constraints  
- Optional multi-language support (Te Reo Māori, Pasifika languages)  

---

## Tech Stack

- Python 3 & FastAPI (Backend)  
- Cohere API (AI recommendations)  
- ChromaDB + Sentence Transformers (Embeddings & search)  
- Frontend built in Visual Studio Code  
- Git + GitHub for version control  

---

## Quick Start

```bash
# Clone repo
git clone git@github.com:Shashiii-Paul/Weyfinder.git
cd Weyfinder

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn cohere chromadb sentence-transformers

# Run backend
cd backend
uvicorn main:app --reload

```

Backend API runs at http://127.0.0.1:8000

## Contact

- Project lead: Natalia
- Backend developer: Shashi
- Frontend developer: Jack
- Coordinate via GitHub repo for frontend/backend collaboration.
