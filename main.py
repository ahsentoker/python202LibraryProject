from book import Book
from library import Library

def main():
    lib = Library()

    while True:
        print("\n--- Kütüphane Menüsü ---")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")
        print("6. ISBN’den Kitap Ekle")  # Aşama 2

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            title = input("Kitap adı: ")
            author = input("Yazar: ")
            isbn = input("ISBN: ")
            lib.add_book(Book(title, author, isbn))
            print("Kitap eklendi.")

        elif secim == "2":
            isbn = input("Silinecek kitabın ISBN'i: ")
            lib.remove_book(isbn)
            print("Kitap silindi.")

        elif secim == "3":
            books = lib.list_books()
            if not books:
                print("Kütüphane boş.")
            else:
                for book in books:
                    print(book)

        elif secim == "4":
            isbn = input("Aranacak kitabın ISBN'i: ")
            book = lib.find_book(isbn)
            if book:
                print(book)
            else:
                print("Kitap bulunamadı.")

        elif secim == "5":
            break

        elif secim == "6":
            isbn = input("ISBN girin: ")
            lib.add_book_by_isbn(isbn)

        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
44