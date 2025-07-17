from models.library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, id, title, author, borrowed_by=None, reserved_by=None):
        """
        Initializes a DVD object by inheriting properties from the LibraryItem class.
        :param id: Unique identifier for the DVD.
        :param title: Title of the DVD.
        :param author: Author/Director of the DVD.
        :param borrowed_by: ID of the user who borrowed the DVD (default is None).
        :param reserved_by: ID of the user who reserved the DVD (default is None).
        """
        # Call the constructor of the parent class (LibraryItem) to initialize shared attributes.
        super().__init__(id=id, title=title, author=author, borrowed_by=borrowed_by, reserved_by=reserved_by)

    def display_info(self):
        """
        Returns a formatted string with information about the DVD.
        Includes details about its title, author, borrowing status, and reservation status.
        :return: A string describing the DVD's details.
        """
        # Determine the borrowing status of the DVD.
        status = f"Borrowed by: {self.borrowed_by}" if self.borrowed_by else "Available"
        # Determine the reservation status of the DVD.
        reservation = f"Reserved by: {self.reserved_by}" if self.reserved_by else "No reservations"
        # Return the formatted details of the DVD.
        return f"[DVD] ID: {self.id}, Title: {self.title}, Author: {self.author}, {status}, {reservation}"

