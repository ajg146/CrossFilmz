
# will have to be big list of all possible tags we get (probably by scraping)
# might be useful to put this in a separate file
tag_list = ['action', 'drama', 'romance', 'mystery']

class Movie:
    def __init__(self, title, given_tags=None, available_platforms=None):
        self.title = title
        self.tags = []
        self.availability = []

        if given_tags is not None:
            self.tags = [tag for tag in given_tags]
        if available_platforms is not None:
            self.availability = [platform for platform in available_platforms]