import sqlite3

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