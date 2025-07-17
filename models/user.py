class User:
    # Initialize the User object with an ID, name, and optional lists for borrowed and reserved items
    def __init__(self, id, name, borrowed_items=None, reserved_items=None):
        self.id = id  # Unique identifier for the user
        self.name = name  # Name of the user
        # List of items borrowed by the user (initialized as empty if not provided)
        self.borrowed_items = borrowed_items if borrowed_items else []  
        # List of items reserved by the user (initialized as empty if not provided)
        self.reserved_items = reserved_items if reserved_items else []

    # Method to borrow an item
    def borrow_item(self, item_id):
        # Check if the item is already borrowed
        if item_id in self.borrowed_items:
            raise Exception(f"Item with ID {item_id} is already borrowed by the user.")
        self.borrowed_items.append(item_id)  # Add the item to the borrowed items list

    # Method to return an item
    def return_item(self, item_id):
        # Check if the item is not in the borrowed items list
        if item_id not in self.borrowed_items:
            raise Exception(f"Item with ID {item_id} is not borrowed by the user.")
        self.borrowed_items.remove(item_id)  # Remove the item from the borrowed items list

    # Method to reserve an item
    def reserve_item(self, item_id):
        # Check if the item is already reserved
        if item_id in self.reserved_items:
            raise Exception(f"Item with ID {item_id} is already reserved by the user.")
        self.reserved_items.append(item_id)  # Add the item to the reserved items list

    # Method to display user information
    def display_info(self):
        return f"User ID: {self.id}, Name: {self.name}, Borrowed Items: {self.borrowed_items}, Reserved Items: {self.reserved_items}"
        # Returns a string with the user's ID, name, borrowed items, and reserved items
