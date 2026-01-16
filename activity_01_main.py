""""
Description: A client program written to verify correctness of 
the activity classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Robinpreet Kaur"


from library_item.library_item import LibraryItem
from genre.genre import Genre

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates an instance of the LibraryItem class with valid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        book = LibraryItem(1, "Harry Potter", "J.K Rowling", Genre.FANTASY, False)
        print("LibraryItem")
    except Exception as e:
        print(f"Error:{e}")




    # 2. Using the instance defined above, and the class Accessors, print 
    # each of the attributes of the LibraryItem instance.
    try:
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Genre: {book.genre.name}")
    except Exception as e:
        print(f"Error in accessing attributes: {e}")
    

    

    # 3. Code a statement which creates an instance of the LibraryItem class with one or more invalid inputs.
    # Use your own unique valid values for the inputs to the class.
    try:
        invalid_input = LibraryItem(1, "", "J.K Rowling", Genre.FANTASY, False)

    except Exception as e:
        print(f"Caught an exception: {e}")

if __name__ == "__main__":
    main()