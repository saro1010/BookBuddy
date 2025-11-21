import json

def save_json(books, filename="book.json"):
    # save all books as JSON file
    data = [b.to_dict() for b in books]
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"data exported successfully to '{filename}'")
        return True
    except Exception as e:
        print(f"failed to export data: {e}")
        return False

def load_json(books, filename="book.json"):
    # load books from JSON file
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        books.clear()
        from models.book import Book
        for book_data in data:
            book = Book.from_dict(book_data)
            books.append(book)
        print(f"data imported successfully from '{filename}'")
        return True
    except FileNotFoundError:
        print(f"file '{filename}' not found.")
        return False
    except Exception as e:
        print(f"failed to import data: {e}")
        return False
