import pickle

def save_pickle(books, filename="books.pkl"):
    # save all books to binary pickle file
    try:
        with open(filename, "wb") as f:
            pickle.dump(books, f)
        print(f"data exported successfully to '{filename}' (pickle)")
        return True
    except Exception as e:
        print(f"failed to export data (pickle): {e}")
        return False

def load_pickle(books, filename="books.pkl"):
    # load all books from pickle file
    try:
        with open(filename, "rb") as f:
            loaded_books = pickle.load(f)
        books.clear()
        books.extend(loaded_books)
        print(f"data imported successfully from '{filename}' (pickle)")
        return True
    except FileNotFoundError:
        print(f"file '{filename}' not found.")
        return False
    except Exception as e:
        print(f"failed to import data (pickle): {e}")
        return False
