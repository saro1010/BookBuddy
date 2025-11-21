def view_reading_progress(books):
    # show progress for all books
    if not books:
        print("library is empty!\n")
        return

    print("\nreading progress:\n")
    for book in books:
        progress = book.get_progress()
        status = "completed" if progress == 100 else ""
        print(f"{book.title} - {book.pages_read}/{book.pages} pages read ({progress}%) {status}")
    print()
