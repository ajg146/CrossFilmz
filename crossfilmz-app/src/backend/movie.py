import sqlite3
import db_ops


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

        return rows

    def __init__(self, title, given_tags=None, available_platforms=None):
        self.title = title
        self.tags = []
        self.availability = []

        if given_tags is not None:
            self.tags = [tag for tag in given_tags]
        if available_platforms is not None:
            self.availability = [platform for platform in available_platforms]

        self.add_movie_to_db()
