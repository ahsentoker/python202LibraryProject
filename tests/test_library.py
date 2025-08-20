# tests/test_library.py
import pytest
from book import Book
from library import Library

@pytest.fixture
def test_lib(tmp_path):
    # Geçici bir library.json dosyası oluşturuyoruz
    json_file = tmp_path / "library.json"
    return Library(filename=str(json_file))

def test_add_book(test_lib):
    book = Book("Kitap 1", "Yazar 1", "111")
    test_lib.add_book(book)
    books = test_lib.list_books()
    assert len(books) == 1
    assert books[0].title == "Kitap 1"
    assert books[0].author == "Yazar 1"
    assert books[0].isbn == "111"

def test_remove_book(test_lib):
    book1 = Book("Kitap 1", "Yazar 1", "111")
