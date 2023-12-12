from entities.source import Source

def insert_book(tag, title, author, publish_year, publisher, repository,
                user_id):
    new_book = Source(
        tag,
        title,
        author,
        publish_year,
        publisher
    )
    repository.insert_book(new_book, user_id)

def get_books(repository, user_id):
    books = repository.get_my_books(user_id)
    return books

def delete_all_books(repository):
    repository.delete_all_books()

def delete_my_books(repository, user_id):
    repository.delete_my_books(user_id)
