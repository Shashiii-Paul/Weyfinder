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

## Navigate to project folder
```bash
cd ~/career-advisor-ai
```

## Initialize Git (if not already)
```bash
git init
git remote add origin git@github.com:Shashiii-Paul/Weyfinder.git
git pull origin main --rebase
```

## Configure Git identity
```bash
git config --global user.name "Shushmita Paul"
git config --global user.email "your_email@example.com"
```

## Create and activate Python virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Upgrade pip and install dependencies
```bash
pip install --upgrade pip
pip install fastapi uvicorn requests cohere python-dotenv chromadb sentence-transformers
```

## Set Cohere API key
```bash
export COHERE_API_KEY="your_cohere_api_key_here"
```

## Create .gitignore
```bash
echo -e "venv/\n__pycache__/\n*.pyc" > .gitignore
```

## Stage and commit backend files
```bash
git add main.py data.json .gitignore
git commit -m "Add FastAPI backend and data.json"
```

## Push to GitHub via SSH (make sure SSH key is added to GitHub)
```bash
git push -u origin main
```

## Run the backend server
```bash
uvicorn main:app --reload
```

Backend API runs at http://127.0.0.1:8000

## Contact

- Project lead: Natalia
- Backend developer: Shashi
- Frontend developer: Jack
- Coordinate via GitHub repo for frontend/backend collaboration.
