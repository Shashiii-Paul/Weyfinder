from fastapi import FastAPI, Query
import cohere
import json
import os
import re

# Load dataset
with open("data.json", "r") as f:
    dataset = json.load(f)

# Setup Cohere client
COHERE_API_KEY = os.getenv("CO_API_KEY")
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
    print('Received query params:', {'career_goal': career_goal, 'language': language})
    prompt = f"""
    You are a career advisor. The user wants to achieve the following long-term career goal:

    "{career_goal}"

    Provide the response in {language}. Use culturally appropriate phrasing where possible.
    Include local and online workshops, certifications, courses, programmes, apprenticeships.
    Ensure suggestions are realistic considering practical restrictions (commute, transport, internet).
    Produce a clear, actionable step-by-step plan.

    IMPORTANT: Format your response exactly as follows:
    Pathway Name: <career suggestion>
    Pathway Idea 1: <first idea>
    Pathway Idea 2: <second idea>

    Dataset:
    {json.dumps(dataset, indent=2)}
    """

    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    text = response.generations[0].text.strip()
    print('Cohere raw response:', text)
    match = re.search(r'Pathway Name:\s*(.*)\nPathway Idea 1:\s*(.*)\nPathway Idea 2:\s*(.*)', text)
    if match:
        pathway_name = match.group(1).strip()
        idea1 = match.group(2).strip()
        idea2 = match.group(3).strip()
    else:
        pathway_name = career_goal
        idea1 = idea2 = ''
    print('Parsed values:', {'pathway_name': pathway_name, 'idea1': idea1, 'idea2': idea2})
    # Always return the full raw response for debugging
    return {
        "career_goal": pathway_name,
        "language": language,
        "idea1": idea1,
        "idea2": idea2,
        "raw": text if text else "(No response from Cohere)"
    }
