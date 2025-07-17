class ItemNotAvailableError(Exception):
    """
    Custom exception raised when a library item is currently not available for borrowing or reservation.
    """
    def __init__(self, message="Item is not available."):
        """
        Initialize the exception with a default or custom error message.
        :param message: Error message string (default: "Item is not available.")
        """
        super().__init__(message)
