from pybtex.database import BibliographyData, Entry
from repositories import books_repository
from entities.source import Source

class Bibtex_Service:
    def __init__(self, repository):
        self.repository = repository

    def get_sourves(self):
        return self.repository.get_books()

    def create_entry(self, source):
        for key, item in source.items:
            print(key)
            print(item)

class FakeBookRepository:
    def __init__(self):
        self.books = []

    def get_books(self):
        return self.books

    def insert_book(self, book):
        self.books.append(book)
        return book

book_jaana = Source("JK17", "Jaanan Kirja", "Jaana Virtanen", 1968, "Otava")
repo = FakeBookRepository()
repo.insert_book(book_jaana)

service = Bibtex_Service(repo)


testi = Entry('article', [
    ('author', 'Sanna'),
    ('title', 'terve'),
    ('publisher', 'Otava'),
    ('year', '1999')
])

bibtesti = BibliographyData({'testi' : testi})

print(testi)
print(bibtesti)

bibtesti.to_file('test_file.bib', 'bibtex')
