class Book:
    def __init__(self, title, author, pages=0):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    
finance = Book("Finance 101", "John Doe", 300)
print(finance)  # Output: 'Finance 101' by John Doe (300 pages)
print(repr(finance))