from models.book import Book

class EBook(Book):
    # subclass of Book for digital books
    def __init__(self, title, author, pages, file_size, format_type, note=None):
        # call parent constructor
        super().__init__(title, author, pages, note)
        # add new attributes
        self.file_size = file_size          
        self.format_type = format_type    

    def __str__(self):
        # readable string for EBook
        base_info = super().__str__()
        return f"{base_info} [EBook: {self.file_size}MB, {self.format_type}]"
