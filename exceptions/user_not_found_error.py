class UserNotFoundError(Exception):
    """
    Custom exception raised when a user is not found in the system.
    """
    def __init__(self, message="User not found."):
        """
        Initialize the exception with a default or custom error message.
        :param message: Error message string (default: "User not found.")
        """
        super().__init__(message)
