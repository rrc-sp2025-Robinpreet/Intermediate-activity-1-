"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "Robinpreet Kaur"
__version__ = "1.0.0"

import unittest
from library_item.library_item import LibraryItem 
from genre.genre import Genre 

class TestLibraryItem(unittest.TestCase):
    """
    Unit tests for the LibraryItem class.
    """

    def setUp(self):
        self.library_item = LibraryItem(1, "Harry Potter", "J.K Rowling", Genre.FANTASY, False)

    def test_init_valid_library_item_attributes_set(self):
        # Act
        library_item = LibraryItem(1, "Harry Potter", "J.K Rowling", Genre.FANTASY, False)
        
        # Assert
        self.assertEqual(library_item._LibraryItem__item_id, 1)
        self.assertEqual(library_item._LibraryItem__title, "Harry Potter")
        self.assertEqual(library_item._LibraryItem__author, "J.K Rowling")
        self.assertEqual(library_item._LibraryItem__genre, Genre.FANTASY)
        self.assertEqual(library_item._LibraryItem__is_borrowed, False)

    def test_init_title_blank_raises_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem(1, "", "J.K Rowling", Genre.FANTASY, False)
    
    def test_init_author_blank_raises_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem(1, "Harry Potter", "", Genre.FANTASY, False)

    def test_init_invalid_genre_raises_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem(1, "Harry Potter", "J.K Rowling", "Fantasy", False)
    
    def test_init_invalid_item_id_raises_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem("abc", "Harry Potter", "J.K Rowling", Genre.FANTASY, False)

    def test_init_invalid_is_borrowed_raises_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem(1, "Harry Potter", "J.K Rowling", Genre.FANTASY, "Yes")

    def test_title_accessor_valid_library_item_title_returned(self):
        # Arrange
        expected = "Harry Potter"

        # Act 
        actual = self.library_item.title

        # Assert
        self.assertEqual(expected, actual)

    def test_author_accessor_valid_library_item_author_returned(self):
        # Arrange
        expected = "J.K Rowling"

        # Act
        actual = self.library_item.author

        # Assert
        self.assertEqual(expected, actual)

    def test_genre_accessor_valid_library_item_genre_returned(self):
        # Arrange
        expected = Genre.FANTASY

        # Act
        actual = self.library_item.genre

        # Assert
        self.assertEqual(expected, actual)

    def test_item_id_accessor_returns_item_id(self):
        expected = 1
        actual = self.library_item.item_id
        self.assertEqual(expected, actual)

    def test_is_borrowed_accessor_returns_is_borrowed(self):
        expected = False
        actual = self.library_item.is_borrowed
        self.assertEqual(expected, actual)
    

if __name__ == "main":
    unittest.main()