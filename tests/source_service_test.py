import unittest
from entities.source import Source
from services import source_service

class FakeBookRepository:
    def __init__(self):
        self.books = []

    def get_my_books(self, uid):
        if uid:
            return self.books #For pylint
        return self.books

    def insert_book(self, book, uid):
        self.books.append(book)
        if uid:
            return book #For pylint
        return book

class TestSourceService(unittest.TestCase):
    def setUp(self):
        self.repo_stub = FakeBookRepository()
        self.book_jaana = Source("JK17", "Jaanan Kirja",
                                  "Jaana Virtanen", 1968, "Otava")

    def test_insert_book_stores_book_object_correctly(self):
        source_service.insert_book(self.book_jaana.latex_key,
                    self.book_jaana.title,
                    self.book_jaana.author,
                    self.book_jaana.publish_year,
                    self.book_jaana.publisher,
                    self.repo_stub, 0)

        books = self.repo_stub.get_my_books(0)

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].latex_key, self.book_jaana.latex_key)
        self.assertEqual(books[0].author, self.book_jaana.author)
        self.assertEqual(books[0].publish_year, self.book_jaana.publish_year)
        self.assertEqual(books[0].publisher, self.book_jaana.publisher)

    def test_get_books_returns_correct_list(self):
        self.repo_stub.books.append(self.book_jaana)
        books = source_service.get_books(self.repo_stub, 0)

        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].latex_key, self.book_jaana.latex_key)
        self.assertEqual(books[0].author, self.book_jaana.author)
        self.assertEqual(books[0].publish_year, self.book_jaana.publish_year)
        self.assertEqual(books[0].publisher, self.book_jaana.publisher)
