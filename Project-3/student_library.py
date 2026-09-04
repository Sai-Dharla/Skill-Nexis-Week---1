class Library:
    def __init__(self, list_of_books):
        """Initialize the library with a list of books."""
        self.books = list_of_books
    def display_available_books(self):
        """Displays all available books in the library."""
        print("\n--- Available Books ---")
        for index, book in enumerate(self.books):
            print(f"{index + 1}. {book}")
        print("-----------------------")
    def borrow_book(self, book_name):
        """Handles borrowing a book."""
        if book_name in self.books:
            print(f"You have been issued '{book_name}'. Please keep it safe and return it within 30 days.")
            self.books.remove(book_name)
            return True
        else:
            print(f"Sorry, '{book_name}' is currently not available or doesn't belong to this library.")
            return False
    def return_book(self, book_name):
        """Handles returning a book."""
        print(f"Thank you for returning '{book_name}'. Hope you enjoyed reading it!")
        self.books.append(book_name)
class Student:
    def request_book(self):
        """Takes input from the student for a book to borrow."""
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    def return_book(self):
        """Takes input from the student for a book to return."""
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
def main():
    # Initialize the library with a starting list of books
    initial_books = [
        "Python Crash Course",
        "Automate the Boring Stuff with Python",
        "Clean Code",
        "The Pragmatic Programmer",
        "Introduction to Algorithms"
    ]
    central_library = Library(initial_books)
    student = Student()
    while True:
        print("\n====== Central Student Library ======")
        print("1. Display Available Books")
        print("2. Request/Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        print("=====================================")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            central_library.display_available_books()
        elif choice == "2":
            requested_book = student.request_book()
            central_library.borrow_book(requested_book)
        elif choice == "3":
            returned_book = student.return_book()
            central_library.return_book(returned_book)
        elif choice == "4":
            print("Thanks for using the Central Student Library! Goodbye.")
            break
        else:
            print("Invalid choice! Please select a valid menu option (1-4).")
if __name__ == "__main__":
    main()