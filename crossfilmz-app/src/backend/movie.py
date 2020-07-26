import sqlite3
import db_ops

# Print movie titles in a way that's easy to view
def pretty_print_movies(movies):
    for movie in movies:
        print(movie[0])


class Movie:
    def add_movie_to_db(self):
        conn, cur = db_ops.open_db_conn()

        sql_command = """
            SELECT *
            FROM movies
            WHERE title = ?"""
        cur.execute(sql_command, (self.title,))

        if cur.fetchone() is None:
            sql_command = """
                INSERT INTO movies
                (title, tags, availability)
                VALUES (?, ?, ?)"""
            cur.execute(sql_command, (self.title, repr(self.tags),
                                      repr(self.availability)))

        db_ops.close_db_conn(conn)

    @staticmethod
    def filter_duplicates(rows):
        new_movies = []
        for row in rows:
            for movies in rows:
                for movie in movies:
                    if movie not in new_movies:
                        new_movies.append(movie)

        return new_movies

    @staticmethod
    def select_all_movies():
        conn, cur = db_ops.open_db_conn()
        sql_command = """
            SELECT *
            FROM movies"""
        cur.execute(sql_command)

        rows = cur.fetchall()
        d = {}
        for r in rows:
            title = r[0]
            genre = r[1]
            platforms = r[2]
            poster = r[3]

        db_ops.close_db_conn(conn)
        print(Movie.filter_duplicates(rows))
        return Movie.filter_duplicates(rows)

    @staticmethod
    def select_some_movies(platforms):
        if isinstance(platforms, str):
            platforms = [platforms]

        rows = []
        conn, cur = db_ops.open_db_conn()

        for platform in platforms:
            query = "SELECT * FROM movies \
                     WHERE availability LIKE '%{}%'".format(platform)
            cur.execute(query)
            rows.append(cur.fetchall())

        db_ops.close_db_conn(conn)
        return Movie.filter_duplicates(rows)

    def __init__(self, title, given_tags=None, available_platforms=None):
        self.title = title
        self.tags = []
        self.availability = []

        if given_tags is not None:
            self.tags = [tag for tag in given_tags]
        if available_platforms is not None:
            self.availability = [platform for platform in available_platforms]

        self.add_movie_to_db()

# FOR VALIDATION:
# def main():
#     pretty_print_movies(Movie.select_some_movies('Netflix'))
#     pretty_print_movies(Movie.select_some_movies(['Netflix', 'Amazon Instant Video']))
#
# if __name__ == "__main__":
#     main()