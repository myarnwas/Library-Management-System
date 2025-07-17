# Import necessary modules and classes
import json # For working with JSON files
from models.library import Library # Library class to manage library operations
from models.book import Book # Class for Book items
from models.dvd import DVD # Class for DVD items
from models.user import User
from models.library_item import LibraryItem
from models.magazine import Magazine
from exceptions.item_not_found_error import ItemNotFoundError
from exceptions.user_not_found_error import UserNotFoundError
from exceptions.item_not_available_error import ItemNotAvailableError
from typing import List, Union

def create_item_from_dict(item: Union[dict, LibraryItem]) -> LibraryItem:
    # إذا جاء كائن جاهز، أعده كما هو
    if isinstance(item, LibraryItem):
        return item

    # يجب أن يكون dict
    if not isinstance(item, dict):
        raise TypeError(f"Expected dict or LibraryItem, got {type(item).__name__}")

    if "type" not in item:
        raise KeyError("'type' key is missing in the item dictionary.")

    item_type = item["type"]
    data = item.copy()
    del data["type"]

    if item_type == "Book":
        return Book(**data)
    elif item_type == "Magazine":
        return Magazine(**data)
    elif item_type == "DVD":
        return DVD(**data)
    else:
        raise ValueError(f"Unknown item type: {item_type}")

# ────────────────────────
# 3) الحفظ والتحميل من JSON
# ────────────────────────
def save_data(file_path: str, items: List[LibraryItem]) -> None:
    """يُسجِّل العناصر إلى JSON."""
    json_data = [item.to_dict() for item in items]
    # json.dump يقبل القواميس والقوائم فقط :contentReference[oaicite:0]{index=0}
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


def load_data(file_path: str, expect_type_key: bool = True) -> list:
    """يقرأ ملف JSON ويعيد قائمة كائنات إذا كانت تحتوي على type، أو قواميس عادية إذا لا."""
    with open(file_path, "r", encoding="utf-8") as file:
        raw_items = json.load(file)
        if expect_type_key:
            return [create_item_from_dict(x) for x in raw_items]
        else:
            return raw_items  # قواميس عادية مثل المستخدمين

def main():
    library = Library()

    raw_items = load_data('data/items.json')
    library.items = [create_item_from_dict(item) for item in raw_items]
    #library.items = [Book(**item_dict) for item_dict in raw_items]

    raw_users = load_data('data/users.json', expect_type_key=False)
    library.users = [User(**user_dict) for user_dict in raw_users]

    while True:
        print("\nWelcome to the Library System")
        print("1. View all available items")
        print("2. Search item by title or type")
        print("3. Register a new user")
        print("4. Borrow an item")
        print("5. Reserve an item")
        print("6. Return an item")
        print("7. Exit and Save")
        choice = input("Select an option: ")

        try:
            if choice == '1':
                for item in library.items:
                    print(item.display_info())

            elif choice == '2':
                keyword = input("Enter search keyword: ")
                results = library.search_items(keyword)
                for item in results:
                    print(item.display_info())

            elif choice == '3':
                name = input("Enter your name: ")
                user_id = input("Enter your ID: ")
                #user_id = library.register_user(name)
                print(f"User registered successfully with ID: {user_id}")

            elif choice == '4':
                user_id = input("Enter your user ID: ")
                item_id = input("Enter the item ID: ")
                library.borrow_item(user_id, item_id)
                print("Item borrowed successfully.")

            elif choice == '5':
                user_id = input("Enter your user ID: ")
                item_id = input("Enter the item ID: ")
                library.reserve_item(user_id, item_id)
                print("Item reserved successfully.")

            elif choice == '6':
                user_id = input("Enter your user ID: ")
                item_id = input("Enter the item ID: ")
                library.return_item(user_id, item_id)
                print("Item returned successfully.")

            elif choice == '7':
                save_data('data/items.json', [item.__dict__ for item in library.items])
                save_data('data/users.json', [user.__dict__ for user in library.users])
                print("Data saved successfully. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        except (ItemNotFoundError, UserNotFoundError, ItemNotAvailableError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
