from models.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, id, title, author, borrowed_by=None, reserved_by=None):
        """
        Initialize a Book object, inheriting from LibraryItem.
        :param id: Unique identifier for the book.
        :param title: Title of the book.
        :param author: Author of the book.
        :param borrowed_by: User ID who borrowed the book (default None).
        :param reserved_by: User ID who reserved the book (default None).
        """
        # Call the parent constructor to set common attributes
        super().__init__(id=id, title=title, author=author, borrowed_by=borrowed_by, reserved_by=reserved_by)

    def display_info(self):
        """
        Returns a formatted string showing book details including borrowing and reservation status.
        :return: Information string about the book.
        """
        # Check if the book is borrowed and prepare status message
        status = f"Borrowed by: {self.borrowed_by}" if self.borrowed_by else "Available"
        # Check if the book is reserved and prepare reservation message
        reservation = f"Reserved by: {self.reserved_by}" if self.reserved_by else "No reservations"
        # Return the combined information string
        return f"[Book] ID: {self.id}, Title: {self.title}, Author: {self.author}, {status}, {reservation}"
    
    