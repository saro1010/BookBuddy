class Book:
    def __init__(self, title, author, pages, note=None):
        # initialize book attributes
        self.title = title 
        self.author = author
        self.pages = pages 
        self.note = note 
        self.pages_read = 0
        
    def log_reading(self, pages): 
        # update read pages
        if pages <= 0:
            print('pages must be greater than zero!')
            return
        self.pages_read += pages
        if self.pages_read > self.pages:
            self.pages_read = self.pages
        print(f"you have read {self.pages_read}/{self.pages} pages.")

    def get_progress(self):
        # calculate progress in percentage
        return round((self.pages_read / self.pages) * 100, 2)

    def to_dict(self):
        # convert Book to dict
        return {
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "pages_read": self.pages_read,
            "note": self.note
        }

    @classmethod
    def from_dict(cls, data):
        # recreate Book object from dict
        book = cls(
            title=data["title"],
            author=data["author"],
            pages=int(data["pages"]),
            note=data.get("note", "")
        )
        book.pages_read = int(data.get("pages_read", 0))
        return book

    def __str__(self):
        # readable string format
        note = self.note if self.note else ""
        note_explain = "--Note : " if self.note else ""     
        return f"{self.title} by {self.author} {note_explain}{note} ({self.get_progress()}% read)"
