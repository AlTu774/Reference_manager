from pybtex.database import BibliographyData, Entry
from entities.source import Source

class Bibtex_Service:
    def __init__(self, repository):
        self.repository = repository

    def create_bibtex_file(self):
        sources = self.repository.get_books()
        entries = []
        for source in sources:
            entries.append(self._create_entry(source))

    def _create_entry(self, source):
        for key, item in source.items():
            print(key)
            print(item)
        return('hi')



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
