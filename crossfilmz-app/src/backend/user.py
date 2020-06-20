import sqlite3
import db_ops
from movie import Movie

MIN_SCORE = 1 # maybe put these in their own file so frontend can reference them too
MAX_SCORE = 5


class User:
    def add_user_to_db(self):
        conn, cur = db_ops.open_db_conn()

        sql_command = """
            SELECT *
            FROM users
            WHERE login = ?"""
        cur.execute(sql_command, (self.login,))

        if cur.fetchone() is None:
            sql_command = """
                INSERT INTO users
                (login)
                VALUES (?)"""
            cur.execute(sql_command, (self.login,))

        db_ops.close_db_conn(conn)

    def add_rating(self, movie, score):
        conn, cur = db_ops.open_db_conn()

        if score < MIN_SCORE or score > MAX_SCORE:
            return # Make this be a more informative exception

        if movie.title not in self.ratings:
            for tag in movie.tags:
                self.vector[tag] = self.vector[tag] + score if tag in self.vector else score
        else:
            previous_rating = self.ratings[movie.title]
            for tag in movie.tags:
                self.vector[tag] += (self.vector[tag] - previous_rating)
        self.ratings[movie.title] = score

        db_ops.close_db_conn(conn)

    def __init__(self, login):
        self.login = login
        self.vector = {}
        self.ratings = {}
        self.add_user_to_db()

# Using for testing
def main():
    user = User('aep67')
    movie = Movie('testmovie', ['action', 'drama'])
    user.add_rating(movie, 2)
    movie2 = Movie('other', ['action', 'comedy'])
    user.add_rating(movie2, 5)

if __name__ == "__main__":
    main()