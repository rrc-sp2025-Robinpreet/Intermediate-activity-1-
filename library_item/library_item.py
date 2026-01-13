""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Robinpreet Kaur"
__version__ = ""

from genre.genre import Genre


class LibraryItem:
    """Represents item in the library."""
    
    def __init__(self, item_id: int, title: str, author: str, genre: Genre, is_borrowed: bool):
        """
        Initializes a LibraryItem object based on received arguments.

        args:
            item_id (int): An id number to uniquely identify the library item.
            title (str):  The title of the library item.
            author (str): The author of the library item.
            genre (Genre): The Genre of the library item.
            is_borrowed (bool):  Identifies whether the library item is borrowed (True) or available (False).
        
        raises:
            ValueError: if any of the arguments are invalid.
        """

        if isinstance(item_id, int):
            self.__item_id = item_id
        else:
            raise ValueError("Item Id must be numeric")

        if isinstance(title, str) and len(title.strip()) > 0: 
            self.__title = title 
        else:
            raise ValueError("Title cannot be blank.")
        
        if isinstance(author, str) and len(author.strip()) > 0:
            self.__author = author
        else:
            raise ValueError("Author cannot be blank.")
        
        if isinstance(genre, Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre.")
        
        if isinstance(is_borrowed, bool):
            self.__is_borrowed = is_borrowed
        else:
            raise ValueError("Is Borrowed must be a boolean value.")
    
    @property
    def item_id(self) -> int:
        """
        Returns:
            int: An id number to uniquely identify the library item. 
        """
        return self.__item_id

    @property
    def title(self) -> str:
        """
        Returns:
            str: The title of the library item.
        """
        return self.__title
    
    @property
    def author(self) -> str:
        """
        Returns:
            str: The author of the library item.
        """
        return self.__author
    
    @property
    def genre(self) -> Genre:
        """
        Returns:
            Genre: The genre of the library item.
        """
        return self.__genre
    
    @property
    def is_borrowed(self) -> bool:
        """
        Returns:
            bool: Identifies whether the library item is borrowed (True) or available (False).
        """
        return self.__is_borrowed
