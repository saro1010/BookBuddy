from models.book import Book

class AudioBook(Book):
    # subclass of Book for audio versions
    def __init__(self, title, author, pages, duration, narrator, note=None):
        # call parent constructor
        super().__init__(title, author, pages, note)
        # add new attributes
        self.duration = duration        # total time in minutes
        self.narrator = narrator        # voice actor name

    def __str__(self):
        # readable string for AudioBook
        base_info = super().__str__()
        return f"{base_info} [AudioBook: {self.duration}min, Narrator: {self.narrator}]"
