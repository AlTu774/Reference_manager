from pybtex.database import BibliographyData, Entry
from entities.source import Source
from services import source_service

class Bibtex_Service:
    def __init__(self, service = source_service):
        self.source_service = service

    def create_bibtex_data(self):
        sources = self.source_service.get_books()
        entries = {}
        for source in sources:
            if type(source != dict):
                source = source._mapping
            entries[source["tag"]] = self._create_entry(source)
        return BibliographyData(entries)

    def create_bibtex_file(self, name):
        self.create_bibtex_data().to_file(f"bibtex_files/{name}.bib", 'bibtex')


    def _create_entry(self, source):
        fields = []
        for key, item in source.items():
            if key == "tag" or key == "ID":
                continue
            fields.append((key, str(item)))
        return Entry('book', fields)
