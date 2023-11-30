from pybtex.database import BibliographyData, Entry
from entities.source import Source
from services import source_service

def create_bibtex_data(source_service):
    sources = source_service.get_books()
    entries = {}
    for source in sources:
        if type(source) != dict:
            source = source._mapping
        entries[source["tag"]] = create_entry(source)
    return BibliographyData(entries)

def create_bibtex_file(name, source_service):
    create_bibtex_data(source_service).to_file(f"bibtex_files/{name}.bib", 'bibtex')


def create_entry(source):
    fields = []
    for key, item in source.items():
        if key == "tag" or key == "ID":
            continue
        fields.append((key, str(item)))
    return Entry('book', fields)
