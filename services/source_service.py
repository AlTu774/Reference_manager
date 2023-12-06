from entities.source import Source
from repositories import books_repository

def insert_book(tag, title, author, publish_year, publisher, repository):
    new_book = Source(
        tag,
        title,
        author,
        publish_year,
        publisher
    )
    repository.insert_book(new_book)

def get_books(repository = books_repository):
    books = repository.get_books()
    return books

def delete_all_books(repository):
    repository.delete_all_books()
