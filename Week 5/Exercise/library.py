class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability_status = True

    def display_book_details(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}"
    
    def update_status(self,status):
        self.availability_status = status

class User:
    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.name = user_name
        self.books_borrowed = []

    def display_user(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Books Borrowed: "
    
    def borrow_book(self, books_title):
        self.books_borrowed.append(books_title)
        return f"Books borrowed: {self.books_borrowed}"
        
    def return_book(self, books_title):
        self.books_borrowed.remove(books_title)

class Library:
    def __init__(self, users, books):
        self.users = []
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def borrowed_books(self, books_title):
        self.books.append(books_title)

    def returned_books(self, books_title):
        self.borrowed_books.remove(books_title)

    def transaction(self):
        pass

class Transaction:
    def __init__(self, borrowed_book, returned_book):
        pass
    
    def record_transaction(self):
        pass

    def generate_transaction(self):
        pass