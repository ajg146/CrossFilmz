
# will have to be big list of all possible tags we get (probably by scraping)
# might be useful to put this in a separate file
tag_list = ['action', 'drama', 'romance', 'mystery']

class Movie:
    def __init__(self, title, given_tags):
        self.title = title
        self.tags = {}

        for tag in tag_list:
            self.tags[tag] = 1 if tag in given_tags else 0