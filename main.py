from models.book import Book
from storage.data_exporter import export_data, import_data
from services.reading_tracker import log_reading
from services.progress_manager import view_reading_progress
from utils.decorators import log_action

books = []  # list to store all Book objects

@log_action
def add_book():
    # get book info from user
    title = input("please enter the book title: ").strip()
    author = input("please enter the book author: ").strip()
    pages = input("please enter the book pages: ").strip()
    note = input("please enter the book note: ").strip()

    # basic validation
    if not title or not author or not pages.isdigit() or int(pages) <= 0:
        print("invalid input!\n")
        return

    # create and add book
    book = Book(title, author, int(pages), note)
    books.append(book)
    print(f"book '{title}' added successfully.\nReturning to main menu...")

@log_action
def view_books():
    # show all books or warn if empty
    if not books:
        print("library is empty!\n")
        return

    print("list of all books:\n")
    for num, book in enumerate(books, 1):
        print(f"{num}. {book}")
    print("Returning to main menu....")

def main():
    while True:
        # main CLI menu
        print("\n1. Add new book")
        print("2. View all books")
        print("3. Log reading pages")
        print("4. View reading progress")
        print("5. Export data")
        print("6. Import data")
        print("7. Exit")
        choice = input("Enter choice: ").strip()

        # handle user choice
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            log_reading(books)
        elif choice == "4":
            view_reading_progress(books)
        elif choice == "5":
            fmt = input("choose format (json/pickle): ").strip().lower() or "json"
            export_data(books, fmt)
        elif choice == "6":
            fmt = input("choose format (json/pickle): ").strip().lower() or "json"
            import_data(books, fmt)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

# run the CLI
if __name__ == "__main__":
    main()
