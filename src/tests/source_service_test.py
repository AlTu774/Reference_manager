import unittest
from services.source_service import (SourceService)
from entities.source import Source


class FakeBookRepository:
    def __init__(self):
        self.books = []

    def get_all_books(self):
        return self.books

    def insert_book(self, book):
        self.books.append(book)
        return book
    
class TestSourceService(unittest.TestCase):
    def setUp(self):
        self._source_service = SourceService()
        self.book_jaana = Source("JK17", "Jaanan Kirja", "Jaana Virtanen", 1968, "Otava")

    def test_insert_book_stores_book_object_correctly(self):
        self._source_service.create_book(self.book_jaana.tag,
                    self.book_jaana.title,
                    self.book_jaana.author,
                    self.book_jaana.publish_year,
                    self.book_jaana.publisher,
                    FakeBookRepository)

        books = self._source_service.get_all_books(FakeBookRepository)

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].tag, self.book_jaana.tag)
