import unittest
from entities.source import Source
from services import source_service
from services.bibtex_service import Bibtex_Service

class FakeBookRepository:
    def __init__(self):
        self.books = [Source("JK17", "Jaanan Kirja", "Jaana Virtanen", 1968, "Otava")]

    def get_books(self):
        return self.books

    def insert_book(self, book):
        self.books.append(book)
        return book
    
class TestSourceService(unittest.TestCase):
    def setUp(self):
        self.repo_stub = FakeBookRepository()
        self.bibtex_service = Bibtex_Service(self.repo_stub)

    def test_service(self):
        self.bibtex_service.create_bibtex_file()