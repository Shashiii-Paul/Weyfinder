import requests
from googletrans import Translator

translator = Translator()

def fetch_courses(query, lang="en"):
    # Example API (replace with actual course APIs)
    url = f"https://api.example.com/courses?search={query}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = [course["title"] + " - " + course["link"] for course in data.get("courses", [])]

        # Translate results if not English
        if lang != "en":
            results = [translator.translate(text, dest=lang).text for text in results]

        return results
    else:
        return [f"Error fetching data: {response.status_code}"]

# Example test
if __name__ == "__main__":
    print(fetch_courses("cybersecurity", "es"))  # fetch and translate to Spanish
