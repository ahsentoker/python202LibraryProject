import pytest
from library import Library

def test_add_book_by_isbn():
    lib = Library(filename="test_library_api.json")
    isbn = "9780140449136"  # Crime and Punishment
    lib.add_book_by_isbn(isbn)  # API’den veri çekme fonksiyonu
    book = lib.find_book(isbn)
    assert book is not None
    assert "Crime" in book.title
