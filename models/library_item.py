class LibraryItem:
    def __init__(self, id, title, author, borrowed_by=None, reserved_by=None, type=None):
        """
        Initializes a LibraryItem object.
        :param id: Unique identifier for the library item.
        :param title: Title of the library item.
        :param author: Author of the library item.
        :param borrowed_by: ID of the user who borrowed the item (default is None).
        :param reserved_by: ID of the user who reserved the item (default is None).
        """
        
        self.id = id  # Assign a unique ID to the library item.
        self.title = title  # Assign a title to the library item.
        self.author = author  # Assign an author to the library item.
        self.borrowed_by = borrowed_by  # Track which user has borrowed the item.
        self.reserved_by = reserved_by  # Track which user has reserved the item.
        self.type = type or self.__class__.__name__
    def display_info(self):
        """
        A placeholder method to display information about the library item.
        Should be overridden by subclasses to provide specific details.
        """
        pass  # No implementation here; meant to be defined in child classes.
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "borrowed_by": self.borrowed_by,   
            "reserved_by": self.reserved_by,
            "type": self.__class__.__name__   # ← يُضاف تلقائياً

        }