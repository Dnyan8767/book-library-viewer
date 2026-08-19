from flask import Flask, render_template

app = Flask(__name__)

# Sample library data (in a real app this would come from a database)
books = {
    1: {"title": "Clean Code", "author": "Robert C. Martin", "genre": "Programming", "year": 2008, "available": True},
    2: {"title": "Deep Learning", "author": "Ian Goodfellow", "genre": "AI/ML", "year": 2016, "available": False},
    3: {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History", "year": 2011, "available": True},
    4: {"title": "The Pragmatic Programmer", "author": "David Thomas", "genre": "Programming", "year": 1999, "available": True},
    5: {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-Help", "year": 2018, "available": False},
}


def get_stats(catalog: dict) -> dict:
    """Compute simple library statistics."""
    total = len(catalog)
    available = sum(1 for b in catalog.values() if b["available"])
    return {
        "total": total,
        "available": available,
        "checked_out": total - available,
    }


@app.route("/")
def index():
    book_list = [{"id": book_id, **details} for book_id, details in books.items()]
    stats = get_stats(books)
    return render_template("index.html", books=book_list, stats=stats)


if __name__ == "__main__":
    app.run(debug=True)