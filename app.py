import os
import requests
import uuid
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='static')

def get_books_from_google(query):
    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=6'
    response = requests.get(url)
    books = response.json().get('items', [])
    results = []
    for book in books:
        info = book.get('volumeInfo', {})
        results.append({
            'title': info.get('title'),
            'authors': ", ".join(info.get('authors', ['Unknown'])),
            'description': info.get('description', 'No description available.'),
            'genre': ", ".join(info.get('categories', ['Unknown'])),
            'image_url': info.get('imageLinks', {}).get('thumbnail', ''),
            'link': info.get('infoLink', '#'),
            'reviews': book.get('searchInfo', {}).get('textSnippet', 'No reviews available.')
        })
    return results

def get_books_from_openlibrary(query):
    url = f'https://openlibrary.org/search.json?q={query}&limit=6'
    response = requests.get(url)
    books = response.json().get('docs', [])
    results = []
    for book in books:
        results.append({
            'title': book.get('title', 'Unknown'),
            'authors': ", ".join(book.get('author_name', ['Unknown'])),
            'description': book.get('first_sentence', {}).get('value', 'No description available.') if isinstance(book.get('first_sentence'), dict) else 'No description available.',
            'genre': ", ".join(book.get('subject', ['Unknown'])) if 'subject' in book else 'Unknown',
            'image_url': f"https://covers.openlibrary.org/b/id/{book.get('cover_i', '')}-M.jpg" if book.get('cover_i') else '',
            'link': f"https://openlibrary.org{book.get('key', '')}",
            'reviews': "Open Library entry - No detailed reviews available."
        })
    return results

@app.route('/')
def home():
    return render_template('questionnaire.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    user_id = str(uuid.uuid4())

    user_row = pd.DataFrame([{
        "user_id": user_id,
        "genre": data["genre"],
        "liked_books": data["liked_books"],
        "microtropes": data["microtropes"],
        "disliked_microtropes": data["disliked_microtropes"],
        "preferred_author": data["preferred_author"]
    }])
    
    # Create directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    user_row.to_csv("data/user_data.csv", mode="a", index=False, header=not os.path.exists("data/user_data.csv"))

    query = f'{data["genre"]} {data["liked_books"]} {data["microtropes"]} {data["preferred_author"]}'
    books = get_books_from_google(query) + get_books_from_openlibrary(query)

    return render_template("Recommend.html", recommendations=books, user_id=user_id)

@app.route('/feedback/<user_id>', methods=['POST'])
def feedback(user_id):
    fb = request.form["feedback"]
    feedback_row = pd.DataFrame([[user_id, fb]], columns=["user_id", "feedback"])
    
    # Create directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    feedback_row.to_csv("data/feedback.csv", mode="a", index=False, header=not os.path.exists("data/feedback.csv"))
    return render_template("feedback.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
