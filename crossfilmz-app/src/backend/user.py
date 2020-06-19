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

    def _update_rating(self, movie, score, cur):
        sql_command = """
            UPDATE user_ratings
            SET rating = ?
            WHERE login = ?
            AND title = ?"""
        cur.execute(sql_command, (score, self.login, str(movie.title)))

    def add_rating(self, movie, score):
        conn, cur = db_ops.open_db_conn()

        if score < MIN_SCORE or score > MAX_SCORE:
            return # Make this be a more informative exception

        sql_command = """
            SELECT *
            FROM user_ratings
            WHERE title = ?"""
        cur.execute(sql_command, (str(movie.title),))

        if cur.fetchone() is not None:
            print('here')
            self._update_rating(movie, score, cur)

        else:
            sql_command = """
                INSERT INTO user_ratings
                (login, title, rating)
                VALUES (?, ?, ?)"""

            cur.execute(sql_command, (self.login, str(movie.title), score))

        # Check if they already rated the movie - don't increase the count if so
        # For tag in movie's tags update the user's vector i guess
        db_ops.close_db_conn(conn)

    def __init__(self, login):
        self.login = login
        self.vector = {}
        self.add_user_to_db()

# Using for testing
def main():
    user = User('aep67')
    movie = Movie('testmovie')
    user.add_rating(movie, 2)

if __name__ == "__main__":
    main()