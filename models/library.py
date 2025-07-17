from exceptions.item_not_found_error import ItemNotFoundError  # Custom exception for missing items
from exceptions.user_not_found_error import UserNotFoundError  # Custom exception for missing users
from exceptions.item_not_available_error import ItemNotAvailableError  # Custom exception for unavailable items
from models.user import User  # Importing the User model

class Library:
    def __init__(self, items=None, users=None):
        """
        Initializes the Library with optional items and users lists.
        :param items: A list of library items (default is an empty list).
        :param users: A list of library users (default is an empty list).
        """
        self.items = items if items else []  # Initialize items with provided list or an empty list
        self.users = users if users else []  # Initialize users with provided list or an empty list

    def search_items(self, keyword):
        """
        Searches for items by a keyword in their title.
        :param keyword: The keyword to search for.
        :return: A list of items matching the keyword in their title.
        """
        return [item for item in self.items if keyword.lower() in item.title.lower()]

    def borrow_item(self, user_id, item_id):
        """
        Allows a user to borrow an item if it's available.
        :param user_id: ID of the user borrowing the item.
        :param item_id: ID of the item to be borrowed.
        :raises UserNotFoundError: If the user ID is not found.
        :raises ItemNotFoundError: If the item ID is not found.
        :raises ItemNotAvailableError: If the item is already borrowed.
        """
        # Find the user and item by their IDs
        user = next((user for user in self.users if user.id == user_id), None)
        item = next((item for item in self.items if item.id == item_id), None)

        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        if not item:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")
        if item.borrowed_by:
            raise ItemNotAvailableError(f"Item with ID {item_id} is already borrowed.")

        # Mark the item as borrowed and update the user's borrowed list
        item.borrowed_by = user_id
        user.borrow_item(item_id)

    def return_item(self, user_id, item_id):
        """
        Allows a user to return a borrowed item.
        :param user_id: ID of the user returning the item.
        :param item_id: ID of the item to be returned.
        :raises UserNotFoundError: If the user ID is not found.
        :raises ItemNotFoundError: If the item ID is not found.
        :raises Exception: If the item is not borrowed by the user.
        """
        # Find the user and item by their IDs
        user = next((user for user in self.users if user.id == user_id), None)
        item = next((item for item in self.items if item.id == item_id), None)

        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found.")
        if not item:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")
        if item.borrowed_by != user_id:
            raise Exception(f"Item with ID {item_id} is not borrowed by user ID {user_id}.")

        # Mark the item as returned and update the user's borrowed list
        item.borrowed_by = None
        user.return_item(item_id)

    def register_user(self, user_id, name):
        """
        Registers a new user in the library.
        :param user_id: ID of the user to be registered.
        :param name: Name of the user to be registered.
        :return: A success or error message.
        """
       # user_id = len(self.users) + 1
        # Check if the user already exists
        if any(user.id == user_id for user in self.users):
            return f"Error: User with ID {user_id} already exists."
        # Create a new user and add them to the list
        new_user = User(id=user_id, name=name)
        self.users.append(new_user)
        return f"User {name} registered successfully."
    
    def reserve_item(self, user_id, item_id):
        """
        Allows a user to reserve an available item.
        :param user_id: ID of the user reserving the item.
        :param item_id: ID of the item to be reserved.
        :return: A success or error message.
        """
        # Find the user and item by their IDs
        user = next((u for u in self.users if u.id == user_id), None)
        if not user:
            return f"Error: User with ID {user_id} not found."

        item = next((i for i in self.items if i.id == item_id), None)
        if not item:
            return f"Error: Item with ID {item_id} not found."

        # Check if the item is borrowed or already reserved
        if item.borrowed_by:
            return f"Error: Item with ID {item_id} is currently borrowed."
        if item.reserved_by:
            return f"Error: Item with ID {item_id} is already reserved by another user."

        # Mark the item as reserved by the user
        item.reserved_by = user_id
        user.reserve_item(item_id)
        return "Item reserved successfully."
