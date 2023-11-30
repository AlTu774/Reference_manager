from pybtex.database import BibliographyData, Entry
from entities.source import Source
from services import source_service

class Bibtex_Service:
    def __init__(self, service):
        self.source_service = service

    def create_bibtex_file(self):
        sources = self.source_service.get_books()
        entries = {}
        for source in sources:
            entries[source["tag"]] = self._create_entry(source)
        data = BibliographyData(entries)
        data.to_file('bibtex_files/references.bib', 'bibtex')

    def _create_entry(self, source):
        fields = []
        for key, item in source.items():
            if key == "tag":
                continue
            fields.append((key, str(item)))
        return Entry('book', fields)


'''
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
'''