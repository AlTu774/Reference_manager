from pybtex.database import BibliographyData, Entry

def create_bibtex_data(source_service, repository, user_id):
    sources = source_service.get_books(repository, user_id)
    entries = {}
    for source in sources:
        if not isinstance(source, dict):
            source = source._mapping # pylint: disable=protected-access
        entries[source["latex_key"]] = create_entry(source)
    return BibliographyData(entries)

def create_bibtex_file(name, source_service, repository, user_id):
    create_bibtex_data(source_service, repository, user_id).to_file(
        f"bibtex_files/{name}.bib", 'bibtex')

def create_entry(source):
    fields = []
    for key, item in source.items():
        if key in ["latex_key", "id", "publish_year"]:
            continue
        fields.append((key, str(item)))
    if "publish_year" in source:
        fields.append(("year", str(source["publish_year"])))
    return Entry('book', fields)
