from abc import ABC, abstractmethod  # Importing Abstract Base Classes (ABC) and the abstractmethod decorator

class Reservable(ABC):  # Defining an abstract base class named Reservable
    @abstractmethod  # Decorator indicating that this method must be implemented in subclasses
    def reserve(self, user):
        """
        Abstract method for reserving an item for a specific user.
        :param user: The user who wants to reserve the item. 
                     This parameter should typically be an instance of the User class or similar.
        """
        pass  # Placeholder for the method implementation to be provided in derived classes
