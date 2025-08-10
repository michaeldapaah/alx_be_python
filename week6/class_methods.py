class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books created: {cls.total_books}")
    
finance = Book()
econs = Book()
business = Book()

Book.display_total_books()
