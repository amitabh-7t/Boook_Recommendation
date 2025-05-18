
# 📚 AI Book Recommender

A smart, sleek, and personalized AI Book Recommender web app powered by Flask, animated TailwindCSS UI, and live integration with **Google Books API** & **Open Library API**. It uses your preferences to recommend relevant books, displays them beautifully, and collects feedback.

---

## 🚀 Features

- 🧠 AI-powered book recommendations based on:
  - Genre
  - Previously liked books
  - Microtropes
  - Preferred author
- 🌐 Real-time results via:
  - Google Books API
  - Open Library API
- 📘 Modal popup for full book details, reviews, and purchase/download link
- ✨ Smooth animated UI using TailwindCSS (via v0.dev)
- 📩 Feedback submission system with a Thank You page
- 📦 Clean codebase with HTML templates and CSV storage

---

## 📁 Project Structure

```
├── app.py                    # Flask backend
├── books.csv                # (optional) local fallback book data
├── user_data.csv            # Stores user inputs
├── feedback.csv             # Stores feedbacks
├── templates/
│   ├── base.html            # Base layout with Tailwind & animations
│   ├── questionnaire.html   # Input form page
│   ├── Recommend.html       # Book results page with modals
│   ├── feedback.html        # Thank-you page
│   └── 404.html             # Optional custom 404
└── static/                  # (optional) for custom assets
```

---

## 🛠️ Installation & Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ai-book-recommender.git
cd ai-book-recommender
```

### 2. Install Python Packages

```bash
pip install flask pandas requests
```

### 3. Run the Flask App

```bash
python app.py
```

### 4. Open in Browser

Visit [http://localhost:5000](http://localhost:5000)

---

## 🧠 How It Works

- User fills out the **questionnaire**
- Backend uses the form input to:
  - Query **Google Books** and **Open Library** for relevant results
  - Extracts title, authors, genre, description, image URL, and purchase/download links
- Books are displayed as cards, **clickable for modal popup**
- User can submit feedback (saved in `feedback.csv`)

---

## 🖼️ Screenshots

> Add screenshots here of the form, recommendation list, and modal popup if needed.

---

## 📌 APIs Used

- [Google Books API](https://developers.google.com/books/)
- [Open Library API](https://openlibrary.org/developers/api)

> All APIs used are free and require no authentication.

---

## ❤️ Made By

**@AT**  
Made with 💡 logic, 📚 books, and 🧠 machine learning

---

## 🧾 License

MIT License — free to use, modify, and deploy.
