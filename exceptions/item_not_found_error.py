class ItemNotFoundError(Exception):
    """
    Custom exception raised when a library item is not found.
    """
    def __init__(self, message="Item not found."):
        """
        Initialize the exception with a default or custom error message.
        :param message: Error message string (default: "Item not found.")
        """
        super().__init__(message)
