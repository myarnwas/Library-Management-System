from models.library_item import LibraryItem  # Importing the base class LibraryItem

class Magazine(LibraryItem):  # Defining the Magazine class, which inherits from LibraryItem
    def __init__(self, id, title, author, borrowed_by=None, reserved_by=None):
        """
        Initializes a Magazine object.
        :param id: Unique identifier for the magazine.
        :param title: Title of the magazine.
        :param author: Author or publisher of the magazine.
        :param borrowed_by: User ID of the person who borrowed the magazine (default is None if not borrowed).
        :param reserved_by: User ID of the person who reserved the magazine (default is None if not reserved).
        """
        # Call the initializer of the base class LibraryItem
        super().__init__(id=id, title=title, author=author, borrowed_by=borrowed_by, reserved_by=reserved_by)

    def display_info(self):
        """
        Returns a string representation of the magazine's information, including its status.
        :return: A formatted string with the magazine's details.
        """
        # Check if the magazine is borrowed and include the borrowed_by user ID if applicable
        status = f"Borrowed by: {self.borrowed_by}" if self.borrowed_by else "Available"
        # Check if the magazine is reserved and include the reserved_by user ID if applicable
        reservation = f"Reserved by: {self.reserved_by}" if self.reserved_by else "No reservations"
        # Return the formatted string with all magazine details
        return f"[Magazine] ID: {self.id}, Title: {self.title}, Author: {self.author}, {status}, {reservation}"


