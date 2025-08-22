from fastapi import FastAPI, Query
import cohere
import json
import os

# Load dataset
with open("data.json", "r") as f:
    dataset = json.load(f)

# Setup Cohere client
COHERE_API_KEY = os.getenv("2pxlvsfrCxe6IwZfGMXwI2wK8zfIILmrrP62rY2p")
co = cohere.Client(COHERE_API_KEY)

# FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Career Advisor AI is running 🚀"}

@app.get("/recommend")
def recommend(
    career_goal: str = Query(..., description="User's long-term career goal"),
    language: str = Query("English", description="Desired output language")
):
    prompt = f"""
    You are a career advisor. The user wants to achieve the following long-term career goal:

    "{career_goal}"

    Provide the response in {language}. Use culturally appropriate phrasing where possible.
    Include local and online workshops, certifications, courses, programmes, apprenticeships.
    Ensure suggestions are realistic considering practical restrictions (commute, transport, internet).
    Produce a clear, actionable step-by-step plan.

    Dataset:
    {json.dumps(dataset, indent=2)}
    """

    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    return {
        "career_goal": career_goal,
        "language": language,
        "recommendation": response.generations[0].text.strip()
    }
