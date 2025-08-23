from flask import Flask, render_template, redirect, url_for, request, flash, session
import time
import cohere
import os
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Set your Cohere API key here
COHERE_API_KEY = os.environ.get('COHERE_API_KEY', 'YOUR_COHERE_API_KEY')
co = cohere.Client(COHERE_API_KEY)
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generation')
def generation():
    profile = session.get('profile', {})
    raw_response = session.get('raw_response', '')
    print('DEBUG: raw_response at render time:', repr(raw_response))
    return render_template('index.html', profile=profile, raw_response=raw_response)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about_you', methods=['POST'])
def about_you():
    # Collect all optional fields
    name = request.form.get('name', '')
    location = request.form.get('location', '')
    age = request.form.get('age', '')
    experience = request.form.get('experience', '')
    interests = request.form.get('interests', '')
    career_interest = request.form.get('career_interest', '')
    language = session.get('language') or request.form.get('language', '')
    areas = request.form.get('areas', '')

    # Store user info in session for use on generation page
    session['profile'] = {
        'name': name,
        'location': location,
        'age': age,
        'experience': experience,
        'interests': interests,
        'career_interest': career_interest,
        'language': language,
        'areas': areas
    }

    # Build the payload for FastAPI
    payload = {
        'career_goal': career_interest or interests or experience or 'Help me choose a career',
        'language': language or 'English'
    }
    print('Sending payload to FastAPI:', payload)

    try:
        fastapi_url = 'http://127.0.0.1:8000/recommend'
        response = requests.get(fastapi_url, params=payload, timeout=30)
        print('Received response from FastAPI:', response.status_code, response.text)
        if response.status_code == 200:
            data = response.json()
            print('Parsed FastAPI response:', data)
            session['raw_response'] = data.get('raw', '')
            session['pathway_name'] = data.get('career_goal', 'Pathway Name')
            session['idea1'] = data.get('idea1', '')
            session['idea2'] = data.get('idea2', '')
            print('Session values set:', session['pathway_name'], session['idea1'], session['idea2'])
        else:
            session['raw_response'] = ''
            session['pathway_name'] = 'Pathway Name'
            session['idea1'] = session['idea2'] = ''
            flash('The AI service is taking too long or returned an error. Please try again later.', 'error')
    except Exception as e:
        print('Error contacting FastAPI:', e)
        session['raw_response'] = ''
        session['pathway_name'] = 'Pathway Name'
        session['idea1'] = session['idea2'] = ''
        flash('There was an error contacting the AI service. Please try again later.', 'error')
    return redirect(url_for('generation'))

@app.route('/update_pathway_name', methods=['POST'])
def update_pathway_name():
    new_name = request.form.get('pathway_name', '').strip()
    if new_name:
        session['pathway_name'] = new_name
        flash('Pathway name updated!')
    else:
        flash('Pathway name cannot be empty.')
    return redirect(url_for('generation'))

if __name__ == '__main__':
    app.run(debug=True)
