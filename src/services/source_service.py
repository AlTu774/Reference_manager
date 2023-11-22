from src.entities.source import Source

def insert_book(tag, title, author, publish_year, publisher, service):
    new_book = Source(
        tag,
        title,
        author,
        publish_year,
        publisher
    )
    service.insert_book(new_book)