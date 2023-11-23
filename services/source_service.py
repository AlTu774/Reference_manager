from entities.source import Source

def insert_book(tag, title, author, publish_year, publisher, repository):
    new_book = Source(
        tag,
        title,
        author,
        publish_year,
        publisher
    )
    repository.insert_book(new_book)