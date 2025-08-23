from fastapi import FastAPI, Query
import cohere
import json
import os

# Load dataset
with open("data.json", "r") as f:
    dataset = json.load(f)

# Setup Cohere client
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("❌ COHERE_API_KEY environment variable not set.")
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
    # Build the prompt
    prompt = f"""
    You are a career advisor. The user wants to achieve the following long-term goal:
    "{career_goal}"

    Provide the response in {language}.
    Use culturally appropriate phrasing.
    Include local and online workshops, certifications, courses, programmes.
    Ensure suggestions are realistic considering practical restrictions (cost, time, location).
    Produce a clear, actionable step-by-step plan.

    Dataset:
    {json.dumps(dataset, indent=2)}
    """

    # Call Cohere
    response = co.generate(
        model="command-r-plus",  # or "command-r" depending on your plan
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    return {
        "career_goal": career_goal,
        "language": language,
        "recommendation": response.generations[0].text.strip()
    }


    # Extract recommendation text safely
    recommendation = None
    if hasattr(response, "generations") and response.generations:
        recommendation = response.generations[0].text.strip()
    elif hasattr(response, "message") and hasattr(response.message, "content"):
        recommendation = response.message.content[0].text.strip()
    else:
        recommendation = "⚠️ No response generated."

    return {
        "career_goal": career_goal,
        "language": language,
        "recommendation": recommendation
    }

