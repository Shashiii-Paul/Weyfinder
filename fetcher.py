# fetcher.py

import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()

def fetch_courses(query):
    """
    Fetch courses matching the query from multiple sources (NZ + online).
    """
    courses = []
    courses += fetch_aut_courses(query)
    courses += fetch_careers_govt_courses(query)
    courses += fetch_online_courses(query)
    return courses


def fetch_aut_courses(query):
    """
    Scrape AUT course search results as examples.
    """
    url = f"https://www.aut.ac.nz/study/study-options/search-courses?query={query}"
    courses = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            for item in soup.select("a.search-result__title"):
                title = item.get_text(strip=True)
                link = "https://www.aut.ac.nz" + item.get("href")
                courses.append({"title": title, "link": link})
    except Exception:
        pass
    # Fallback example if scraping fails
    if not courses:
        courses.append({"title": f"{query.title()} Course - AUT (example)", 
                        "link": "https://www.aut.ac.nz/study/study-options/search-courses"})
    return courses


def fetch_careers_govt_courses(query):
    """
    Scrape Careers.govt.nz search results.
    """
    url = f"https://www.careers.govt.nz/search/?q={query}"
    courses = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            for item in soup.select("a.career-result__link"):
                title = item.get_text(strip=True)
                link = "https://www.careers.govt.nz" + item.get("href")
                courses.append({"title": title, "link": link})
    except Exception:
        pass
    # Fallback example
    if not courses:
        courses.append({"title": f"{query.title()} Workshop - Careers NZ (example)", 
                        "link": "https://www.careers.govt.nz"})
    return courses


def fetch_online_courses(query):
    """
    Add online courses from Coursera, edX, Udemy.
    """
    online_courses = [
        {"title": f"{query.title()} Online Course - Coursera", "link": "https://www.coursera.org"},
        {"title": f"{query.title()} Online Course - edX", "link": "https://www.edx.org"},
        {"title": f"{query.title()} Online Course - Udemy", "link": "https://www.udemy.com"}
    ]
    return online_courses


def translate_courses(courses, lang="en"):
    """
    Translate course titles to the target language (Te Reo Māori or Pacific languages).
    """
    if lang == "en":
        return courses
    translated = []
    for c in courses:
        try:
            translated_title = translator.translate(c["title"], dest=lang).text
        except Exception:
            translated_title = c["title"]
        translated.append({"title": translated_title, "link": c["link"]})
    return translated


# Example test
if __name__ == "__main__":
    example_courses = fetch_courses("cybersecurity")
    print("English:", example_courses)
    print("Te Reo Māori:", translate_courses(example_courses, "mi"))
    print("Samoan:", translate_courses(example_courses, "sm"))
    print("Tongan:", translate_courses(example_courses, "to"))
