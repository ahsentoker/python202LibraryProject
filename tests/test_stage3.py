import pytest
from fastapi.testclient import TestClient
from api import app
from book import Book
from library import Library

client = TestClient(app)

@pytest.fixture
def empty_library(tmp_path, monkeypatch):
    # Geçici JSON dosyası
    json_file = tmp_path / "test_library.json"
    lib = Library(filename=str(json_file))
    monkeypatch.setattr('api.lib', lib)
    return lib

def test_books_initially_empty(empty_library):
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == []

def test_post_book_and_retrieve(empty_library, monkeypatch):
    monkeypatch.setattr('api.lib', empty_library)

    def mock_add_book_by_isbn(self, isbn):
        return Book(title="Mock Book", author="Mock Author", isbn=isbn)

    monkeypatch.setattr(Library, "add_book_by_isbn", mock_add_book_by_isbn)

    response = client.post("/books", json={
        "title": "Mock Book",
        "author": "Mock Author",
        "isbn": "1234567890"
    })

    assert response.status_code == 200
    assert response.json() == {"message": "Kitap eklendi"}

def test_delete_book_success(empty_library, monkeypatch):
    monkeypatch.setattr('api.lib', empty_library)

    # Önce kitap ekle
    book = Book("Silinecek Kitap", "Silinecek Yazar", "0001112223")
    empty_library.add_book(book)

    # Sonra sil
    response = client.delete("/books/0001112223")
    assert response.status_code == 200
    assert response.json() == {"message": "Kitap silindi"}
