import unittest
from pybtex.database import BibliographyData, Entry
from services import bibtex_service

class FakeBookRepository:
    def __init__(self):
        self.books = [{
            "tag":"JK17","author":"Jaana Virtanen","title":"Jaanan Kirja",
            "publisher":"Otava", "year":1968},
        {"tag":"K","author":"Matti Mäkelä","title":"Joku Kirja",
         "publisher":"Otava", "year":2000}]

    def get_books(self, id):
        return self.books

    def insert_book(self, book):
        self.books.append(book)
        return book

class TestBibtex(unittest.TestCase):
    def setUp(self):
        self.book_repo = FakeBookRepository()
        self.bibtex_s = bibtex_service

    def test_create_entry_correctly(self):
        source = {"tag":"JK17","author":"Jaana Virtanen",
                  "title":"Jaanan Kirja","publisher":"Otava", "year":1968}
        entry = self.bibtex_s.create_entry(source)
        correct_entry = Entry("book",[("author", "Jaana Virtanen"),
        ("title", "Jaanan Kirja"),
        ("publisher","Otava"),
        ("year", "1968"),
        ])
        self.assertEqual(entry, correct_entry)

    def test_create_bibliographydata_correctly(self):
        data = self.bibtex_s.create_bibtex_data(self.book_repo, 0)
        source1 = {"tag":"JK17","author":"Jaana Virtanen",
                   "title":"Jaanan Kirja","publisher":"Otava", "year":1968}
        source2 = {"tag":"K","author":"Matti Mäkelä",
                   "title":"Joku Kirja","publisher":"Otava", "year":2000}
        entry1 = self.bibtex_s.create_entry(source1)
        entry2 = self.bibtex_s.create_entry(source2)
        correct_data = BibliographyData({"JK17":entry1, "K":entry2})
        self.assertEqual(data, correct_data)
