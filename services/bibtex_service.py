from pybtex.database import BibliographyData, Entry

def create_bibtex_data(source_service):
    sources = source_service.get_books()
    entries = {}
    for source in sources:
        if type(source) != dict:
            source = source._mapping
        entries[source["tag"]] = create_entry(source)
    return BibliographyData(entries)

def create_bibtex_file(name, source_service):
    create_bibtex_data(source_service).to_file(
        f"bibtex_files/{name}.bib", 'bibtex')

def create_entry(source):
    fields = []
    for key, item in source.items():
        if key == "tag" or key == "id" or key == "publish_year":
            continue
        fields.append((key, str(item)))
    if "publish_year" in source:
        fields.append(("year", str(source["publish_year"])))
    return Entry('book', fields)
