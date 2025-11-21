def log_reading(books):
    # add reading progress for a specific book
    if not books:
        print("library is empty!\n")
        return

    print("list of all books:\n")
    for i, b in enumerate(books, 1):
        print(f"{i}. {b}")
    print()

    choose = input("Enter the book number: ").strip()
    if not choose.isdigit():
        print("invalid input, please enter an integer!\n")
        return
    id_ = int(choose)
    if not (1 <= id_ <= len(books)):
        print(f"please enter a number from 1 to {len(books)}\n")
        return

    read_pages = input("Enter the number of pages you read: ").strip()
    if not read_pages.isdigit() or int(read_pages) <= 0:
        print("invalid input, please enter a positive integer!\n")
        return

    book = books[id_ - 1]
    book.log_reading(int(read_pages))
    print(f"progress: {book.get_progress()}%\n")
