from storage.json_handler import save_json, load_json
from storage.pickle_handler import save_pickle, load_pickle

def export_data(books, fmt="json"):
    # choose export format
    fmt = (fmt or "json").lower()
    if fmt == "json":
        return save_json(books, filename="book.json")
    if fmt == "pickle":
        return save_pickle(books, filename="books.pkl")
    print("unsupported export format (use 'json' or 'pickle').")
    return False

def import_data(books, fmt="json"):
    # choose import format
    fmt = (fmt or "json").lower()
    if fmt == "json":
        return load_json(books, filename="book.json")
    if fmt == "pickle":
        return load_pickle(books, filename="books.pkl")
    print("unsupported import format (use 'json' or 'pickle').")
    return False
