"""
import unittest
import app
from repositories.books_repository import books_repository
from entities.source import Source

class TestBooksRepository(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.book_jaana = Source("JK17", "Jaanan Kirja", "Jaana Virtanen", 1968, "Otava")

    def test_create_stores_book_source_object_correctly(self):
        books_repository.insert_book(self.book_jaana)
        returned_books = books_repository.get_all_books()

        self.assertEqual(returned_books[0], self.book_jaana)
"""
