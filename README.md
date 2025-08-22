<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weyfinder – Career Path Navigator AI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: auto;
            padding: 20px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            overflow-x: auto;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
        }
        ul {
            margin: 0 0 10px 20px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
    </style>
</head>
<body>

<h1>Weyfinder – Career Path Navigator AI</h1>

<p><strong>Weyfinder</strong> is an AI-powered career navigation tool designed to help people in New Zealand who are uncertain about their career paths. It provides <strong>personalized career guidance</strong>, recommending relevant careers, courses, workshops, certifications, programs, and apprenticeships. The AI considers practical constraints such as commute, transport availability, and internet connectivity, and produces actionable, realistic plans.</p>

<h2>Project Overview</h2>
<ul>
    <li><strong>Backend:</strong> Python FastAPI API that serves AI-generated career pathways.</li>
    <li><strong>AI Integration:</strong> Cohere API for natural language recommendations.</li>
    <li><strong>Data:</strong> <code>data.json</code> contains career paths, online and local courses, workshops, and other learning opportunities.</li>
    <li><strong>Frontend:</strong> UI built in Visual Studio Code that consumes backend API and displays career recommendations to users.</li>
    <li><strong>Version Control:</strong> Git + GitHub for collaboration.</li>
</ul>

<h2>Project Structure</h2>
<pre>
career-advisor-ai/
├── backend/
│   ├── main.py          # FastAPI backend API
│   ├── data.json        # Career & course dataset
│   └── .gitignore       # ignores venv, __pycache__, etc.
├── venv/                # Python virtual environment (ignored)
├── README.md            # This file
</pre>

<h2>Backend Setup (Ubuntu / Local Machine)</h2>

<h3>1. Clone the repository</h3>
<pre>
git clone git@github.com:Shashiii-Paul/Weyfinder.git
cd Weyfinder
</pre>

<h3>2. Set up Python virtual environment</h3>
<pre>
python3 -m venv venv
source venv/bin/activate
</pre>

<h3>3. Install dependencies</h3>
<pre>
pip install --upgrade pip
pip install fastapi uvicorn cohere python-dotenv chromadb sentence-transformers
</pre>

<h3>4. Configure Cohere API key</h3>
<p>Sign up at <a href="https://cohere.ai/" target="_blank">Cohere</a> to get an API key. Set it in your environment:</p>
<pre>
export COHERE_API_KEY="your_cohere_api_key_here"
</pre>

<h3>5. Run the backend</h3>
<pre>
cd backend
uvicorn main:app --reload
</pre>
<p>The backend API will be available at <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>. You can test endpoints using Postman, curl, or directly from the frontend.</p>

<h2>Frontend Setup (Visual Studio Code)</h2>

<h3>1. Clone and pull latest changes</h3>
<pre>
git pull origin main
</pre>

<h3>2. Set up frontend folder</h3>
<p>If a <code>frontend/</code> folder does not exist, create it. Connect frontend to the backend API at <code>http://127.0.0.1:8000</code>.</p>

<h3>3. Workflow</h3>
<ul>
    <li>Frontend calls backend endpoints to fetch AI-generated career recommendations.</li>
    <li>Display recommendations including:
        <ul>
            <li>Career paths</li>
            <li>Local and online courses/workshops</li>
            <li>Actionable plans considering commute and internet constraints</li>
        </ul>
    </li>
</ul>

<h3>4. Optional Features</h3>
<ul>
    <li>Multi-language support: Te Reo Māori, Pasifika languages</li>
    <li>Filtering by practical restrictions (commute distance, internet availability)</li>
    <li>Interactive plan-building and personalization</li>
</ul>

<h2>Git Workflow & Collaboration</h2>
<ul>
    <li>Always pull latest changes before starting work: <pre>git pull origin main</pre></li>
    <li>Stage and commit your changes: <pre>git add .<br>git commit -m "Describe your changes"<br>git push origin main</pre></li>
    <li>Avoid committing virtual environment or cache directories — they are included in <code>.gitignore</code>.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li>Python 3</li>
    <li>FastAPI (Backend API)</li>
    <li>Cohere API (AI for career recommendations)</li>
    <li>ChromaDB + Sentence Transformers (Embeddings & search)</li>
    <li>Visual Studio Code (Frontend UI)</li>
    <li>Git + GitHub (Version control)</li>
</ul>

<h2>Future Improvements</h2>
<ul>
    <li>Expand <code>data.json</code> with additional careers, courses, and programs from <a href="https://www.careers.govt.nz" target="_blank">careers.govt.nz</a>.</li>
    <li>Add multi-language support (Te Reo Māori, Pasifika languages).</li>
    <li>Build enhanced filtering and personalized recommendation options.</li>
    <li>Create a more interactive and user-friendly frontend interface.</li>
</ul>

<h2>Getting Help / Contact</h2>
<p>For questions about the backend, data, or Git workflow, contact <strong>Shushmita Paul</strong> (project lead). For frontend or UI questions, coordinate through the GitHub repository and pull requests.</p>

</body>
</html>
