# Library Management System

#Defining class Book
class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    # Getter for title
    def get_title(self):
        return self._title

    # Setter for title
    def set_title(self, title):
        if not title:
            raise ValueError("Title cannot be empty.")
        self._title = title

    # Getter for author
    def get_author(self):
        return self._author

    # Setter for author
    def set_author(self, author):
        if not author:
            raise ValueError("Author cannot be empty.")
        self._author = author

    # Getter for pages
    def get_pages(self):
        return self._pages

    # Setter for pages
    def set_pages(self, pages):
        if pages <= 0:
            raise ValueError("Number of pages must be positive.")
        self._pages = pages

    # Method to calculate reading time based on words per minute
    @classmethod
    def calculate_reading_time(cls, pages, words_per_minute=250):
        words_per_page = 300  # Average number of words per page
        total_words = pages * words_per_page
        return total_words / words_per_minute

    def __str__(self):
        return f"Book: {self._title}, Author: {self._author}, Pages: {self._pages}"


class Ebook(Book):
    def __init__(self, title, author, pages, format_):
        super().__init__(title, author, pages)
        self._format = format_

    # Getter for format
    def get_format(self):
        return self._format

    # Setter for format
    def set_format(self, format_):
        if not format_:
            raise ValueError("Format cannot be empty.")
        self._format = format_

    # Overriding __str__ method
    def __str__(self):
        return (f"Ebook: {self._title}, Author: {self._author}, "
                f"Pages: {self._pages}, Format: {self._format}")


# Demonstration of the Book class
book = Book("Python Programming", "John Doe", 350)
print(book)

# Demonstrate the use of getter and setter methods
book.set_title("Advanced Python Programming")
book.set_author("Jane Doe")
book.set_pages(400)

print("Title:", book.get_title())
print("Author:", book.get_author())
print("Pages:", book.get_pages())

# Calculating the reading time
reading_time = Book.calculate_reading_time(book.get_pages())
print(f"Estimated reading time: {reading_time:.2f} minutes")

# Demonstration of the Ebook class
ebook = Ebook("Python Programming", "John Doe", 350, "PDF")
print(ebook)

# Exception handling demonstration
try:
    ebook.set_pages(-100)
except ValueError as e:
    print("Error:", e)

try:
    ebook.set_format("")
except ValueError as e:
    print("Error:", e)
