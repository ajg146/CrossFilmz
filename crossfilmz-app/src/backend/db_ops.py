import sqlite3
from user import User
from movie import Movie

# TODO:
# - Add rating: add to ratings table, update user's vector - will have to keep
#   track of how many times a tag has been used for averaging
# - Get recommendations: using matrix mult type stuff - going to be annoying
#   because we will have to parse through all the tags because of how they're
#   stored as one string

def open_db_conn():
    conn = sqlite3.connect('crossfilmz.db')
    cur = conn.cursor()
    return conn, cur

def close_db_conn(conn):
    conn.commit()
    conn.close()

def add_user(user):
    conn, cur = open_db_conn()

    sql_command = """
        SELECT *
        FROM users
        WHERE login = ?"""
    cur.execute(sql_command, (user.login,))

    if cur.fetchone() is None:
        sql_command = """
            INSERT INTO users
            (login)
            VALUES (?)"""
        cur.execute(sql_command, (user.login,))

    close_db_conn(conn)

def add_movie(movie):
    conn, cur = open_db_conn()

    sql_command = """
        SELECT *
        FROM movies
        WHERE title = ?"""
    cur.execute(sql_command, (movie.title,))

    if cur.fetchone() is None:
        sql_command = """
            INSERT INTO movies
            (title, tags)
            VALUES (?, ?)"""
        cur.execute(sql_command, (movie.title, repr(movie.tags)))

    close_db_conn(conn)

def main():
    # Some examples used for verifying
    # user = User('testuser')
    # add_user(user)

    # movie = Movie('testmovie', ['action', 'mystery'])
    # add_movie(movie)

if __name__ == "__main__":
    main()