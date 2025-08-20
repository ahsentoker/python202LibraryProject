import pytest
import respx
import httpx
from book import Book
from library import Library

@pytest.fixture
def sample_library(tmp_path):
    json_file = tmp_path / "stage2_library.json"
    return Library(filename=str(json_file))

@respx.mock
def test_isbn_book_addition_success(sample_library):
    isbn = "9780140328721"
    # Gerçek API çağrısına uygun mock:
    respx.get("https://openlibrary.org/api/books").mock(
        return_value=httpx.Response(200, json={
            f"ISBN:{isbn}": {
                "title": "Matilda",
                "authors": [{"name": "Roald Dahl"}]
            }
        })
    )  # <-- buradaki parantez kapandı

    book = sample_library.add_book_by_isbn(isbn)
    assert isinstance(book, Book)
    assert book.title == "Matilda"
    assert book.author == "Roald Dahl"
    assert book.isbn == isbn

@respx.mock
def test_isbn_book_addition_fail(sample_library):
    isbn = "0000000000"
    respx.get("https://openlibrary.org/api/books").mock(
        return_value=httpx.Response(200, json={})
    )
    book = sample_library.add_book_by_isbn(isbn)
    assert book is None
