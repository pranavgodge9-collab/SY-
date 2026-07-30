class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"ID: {self.patron_id}, Name: {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_available:
            book.is_available = False
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is currently unavailable.")

    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[patron_id]

        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.is_available = True
                patron.borrowed_books.remove(book)
                print(f"{patron.name} returned '{book.title}'.")
                return

        print("Book was not borrowed by this patron.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(book)

    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            print(patron)

library = Library()

library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Alice Brown"))
library.add_book(Book(103, "Machine Learning", "David Lee"))

library.register_patron(Patron(1, "Rahul"))
library.register_patron(Patron(2, "Priya"))

library.display_books()

library.borrow_book(1, 101)
library.borrow_book(2, 102)

library.display_books()

library.return_book(1, 101)

library.display_books()