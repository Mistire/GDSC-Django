class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability_status = True

    def display_book_details(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nAvailability: {'Available' if self.availability_status else 'Not Available'}\n"
    
    def update_status(self,status):
        self.availability_status = status

class User:
    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.name = user_name
        self.books_borrowed = []

    def display_user(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Books Borrowed: {', '.join(self.books_borrowed)}"
    
    def borrow_book(self, books_title):
        if availability_status:
            self.books_borrowed.append(books_title)
            availability_status = False
            print(f"'{books_title}' has been successfully been borrowed by {self.name}")
        else:
            print(f"'{books_title}' isn't available right now")
        return f"Books borrowed: {self.books_borrowed}"
        
    def return_book(self, books_title):
        if books_title in self.books_borrowed:    
            self.books_borrowed.remove(books_title)
            availability_status = True
            print(f"'{books_title}' is been returned to the library by {self.name}")
        else:
            print(f"You haven't borrowed the book '{books_title}' from the library")

class Library:
    def __init__(self, users, books):
        self.users = []
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        print("Books is in the library: ")
        for book in self.books:
            book.display_book_details()

    def register_user(self, user):
        self.users.append(user)
        print(f"User '{user.name}' registered in the library.")

    def display_users(self):
        print("Users Registered in the library: ")
        for user in self.users:
            user.display_user()

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