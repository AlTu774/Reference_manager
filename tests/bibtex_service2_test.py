import unittest
from entities.source import Source
from services.bibtex_service import Bibtex_Service

class FakeBookRepository:
    def __init__(self):
        self.books = [Source("JK17", "Jaanan Kirja", "Jaana Virtanen", 1968, "Otava"),
        Source("K", "Joku Kirja", "Matti Mäkelä", 2000, "Otava")]

    def get_books(self):
        return self.books

    def insert_book(self, book):
        self.books.append(book)
        return book

class TestBibtex(unittest.TestCase):
    def setUp:
        self.book_repo = FakeBookRepository()
        self.bibtex_s = Bibtex_Service(self.repo)
    
    def test_create_entry_correctly(self):
        source = Source("JK17", "Jaanan Kirja", "Jaana Virtanen", 1968, "Otava")
        entry = self.bibtex_s.create_entry(source)
        correct_entry = ("JK17",[("author", "Jaana Virtanen"),
        ("title", "Jaanan Kirja"),
        ("publisher","Jaana Virtanen"),
        ("year", "1968"),
        ])
        self.assertEqual(entry, correct_entry)
    
    def test_create_bibliographydata_correctly(self):
        data = self.bibtex_s.create_bibtex_data()
        source1 = Source("JK17", "Jaanan Kirja", "Jaana Virtanen", 1968, "Otava")
        source2 = Source("K", "Joku Kirja", "Matti Mäkelä", 2000, "Otava")
        entry1 = self.bibtex_s.create_entry(source1)
        entry2 = self.bibtex_s.create_entry(source2)
        correct_data = ({"book":entry1, "book":entry2})
        self.assertEqual(data, correct_data)