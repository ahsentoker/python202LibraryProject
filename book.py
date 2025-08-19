# book.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn  # benzersiz kimlik

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
