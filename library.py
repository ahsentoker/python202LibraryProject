import json
import os
import httpx
from book import Book
from unidecode import unidecode  # Latin harfleri için

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        """JSON dosyasından kitapları yükler."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book(**book_data) for book_data in data]

    def save_books(self):
        """Kitapları JSON dosyasına kaydeder."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([book.__dict__ for book in self.books], f, ensure_ascii=False, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def list_books(self):
        return self.books

    def find_book(self, isbn):
        """ISBN ile kitap bulur."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def add_book_by_isbn(self, isbn):
        """Open Library API'den ISBN ile kitap bilgisi çekip ekler (Latin harfli, sadece isim-soyisim)."""
        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
        try:
            response = httpx.get(url, timeout=10)
            data = response.json()
            key = f"ISBN:{isbn}"
            if key in data:
                book_data = data[key]
                title = book_data.get("title", "Bilinmeyen Başlık")
                authors = book_data.get("authors", [])
                if authors:
                    author_raw = authors[0]["name"]
                    author = ' '.join(author_raw.split()[:2])
                    author = unidecode(author)
                else:
                    author = "Bilinmeyen Yazar"
                new_book = Book(title, author, isbn)
                self.add_book(new_book)
                print(f"Kitap eklendi: {title} by {author} (ISBN: {isbn})")
                return new_book  # Burada döndür
            else:
                print("Kitap bilgisi API'de bulunamadı.")
                return None
        except Exception as e:
            print(f"API isteği başarısız: {e}")
            return None
