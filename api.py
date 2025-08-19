from fastapi import FastAPI, HTTPException
from library import Library
from book import Book
from pydantic import BaseModel

app = FastAPI()
lib = Library()

# Pydantic model: POST ile kitap eklerken kullanacağız
class BookModel(BaseModel):
    title: str
    author: str
    isbn: str

# GET /books → Tüm kitaplar
@app.get("/books")
def get_books():
    return lib.list_books()

# GET /books/{isbn} → ISBN ile kitap bul
@app.get("/books/{isbn}")
def get_book(isbn: str):
    book = lib.find_book(isbn)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Kitap bulunamadı")

# POST /books → Yeni kitap ekle
@app.post("/books")
def add_book(book: BookModel):
    if lib.find_book(book.isbn):
        raise HTTPException(status_code=400, detail="Bu ISBN zaten mevcut")
    lib.add_book(Book(book.title, book.author, book.isbn))
    return {"message": "Kitap eklendi"}

# DELETE /books/{isbn} → Kitap sil
@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    book = lib.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")
    lib.remove_book(isbn)
    return {"message": "Kitap silindi"}
