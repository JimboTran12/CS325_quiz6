class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = False

class LibraryUser:
    def search_books(self, title=None, author=None, genre=None):
        raise NotImplementedError("Subclasses must implement search_books method")

class GuestUser(LibraryUser):
    def search_books(self, title=None, author=None, genre=None):
        # Implement search functionality for guest users
        print("Guest user searching for books by title, author, or genre...")

class RegisteredUser(LibraryUser):
    def search_books(self, title=None, author=None, genre=None):
        # Implement search functionality for registered users
        print("Registered user searching for books by title, author, or genre...")

    def borrow_book(self, book):
        # Implement borrowing functionality for registered users
        print("Registered user borrowing book:", book.title)

    def return_book(self, book):
        # Implement returning functionality for registered users
        print("Registered user returning book:", book.title)

class Librarian(LibraryUser):
    def search_books(self, title=None, author=None, genre=None):
        # Implement search functionality for librarians
        print("Librarian searching for books by title, author, or genre...")

    def add_book(self, book):
        # Implement adding functionality for librarians
        print("Librarian adding book to catalog:", book.title)

    def remove_book(self, book):
        # Implement removing functionality for librarians
        print("Librarian removing book from catalog:", book.title)

    def generate_reports(self):
        # Implement report generation functionality for librarians
        print("Librarian generating reports...")

if __name__ == "__main__":

    book1 = Book("Harry Potter", "J.K. Rowling", "Fantasy")
    guest_user = GuestUser()
    registered_user = RegisteredUser()
    librarian = Librarian()

    guest_user.search_books(author="J.K. Rowling")
    registered_user.borrow_book(book1)
    librarian.add_book(book1)
    librarian.generate_reports()
