class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability_status = True

    def display_books(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}"
    
    def update_status(self,status):
        self.availability_status = status

class User:
    def __init__(self,user_id,name,books_borrowed):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_user(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Books Borrowed: "
    
    def borrow_book(self):
        pass

    def return_book(self):
        pass

class Library:
    def __init__(self, users, books):
        self.users = []
        self.books = []
    
    def add_book(self, book):
        pass


    def register_user(self, user):

        pass
    def transaction(self):
        pass

class Transaction:
    def __init__()