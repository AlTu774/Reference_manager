class Source:
    def __init__(self, latex_key, title, author, publish_year, publisher):
        self.latex_key = latex_key
        self.title = title
        self.author = author
        self.publish_year = int(publish_year)
        self.publisher = publisher
