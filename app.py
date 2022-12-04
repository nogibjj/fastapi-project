from fastapi import FastAPI
import uvicorn
import pandas as pd

# Read in the books dataset
books = pd.read_csv("books.csv", on_bad_lines="skip", index_col="bookID")

app = FastAPI()


@app.get("/")
async def root():
    """Define Root Path"""
    return {"message": "Query for Goodreads book data"}


@app.get("/books/{book_id}")
async def read_user(book_id: int):
    """Get information about a specific book with the book ID"""
    if book_id not in books.index:
        return {"message": "the id you entered is not available"}

    # Get attributes about the book
    title = books.loc[book_id, "title"]
    authors = books.loc[book_id, "authors"]
    rating = books.loc[book_id, "average_rating"]
    publisher = books.loc[book_id, "publisher"]
    isbn = books.loc[book_id, "isbn"]
    language = books.loc[book_id, "language_code"]
    pages = books.loc[book_id, "  num_pages"]
    num_ratings = books.loc[book_id, "ratings_count"]
    num_reviews = books.loc[book_id, "text_reviews_count"]

    return {
        "book_id": book_id,
        "title": title,
        "authors": authors,
        "average rating": int(rating),
        "publisher": publisher,
        "isbn code": isbn,
        "language code": language,
        "number of pages": int(pages),
        "number of ratings posted": int(num_ratings),
        "number of reviews posted": int(num_reviews),
    }


@app.post("/lookup_by_title")
async def lookup_by_title(title: str):
    """Look up the book by title"""
    if (title != books["title"]).all():
        return {"message": "the book title you entered is not available"}
    book = books.loc[books["title"] == title]
    book_id = book.index.values[0]
    authors = book["authors"].values[0]
    rating = book["average_rating"].values[0]
    publisher = book["publisher"].values[0]
    isbn = books["isbn"].values[0]
    language = books["language_code"].values[0]
    pages = books["  num_pages"].values[0]
    num_ratings = books["ratings_count"].values[0]
    num_reviews = books["text_reviews_count"].values[0]
    return {
        "title": title,
        "book_id": int(book_id),
        "authors": authors,
        "average rating": int(rating),
        "publisher": publisher,
        "isbn code": isbn,
        "language code": language,
        "number of pages": int(pages),
        "number of ratings posted": int(num_ratings),
        "number of reviews posted": int(num_reviews),
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
