import sqlite3

def open_db_conn():
    conn = sqlite3.connect('crossfilmz.db')
    cur = conn.cursor()
    return conn, cur

def close_db_conn(conn):
    conn.commit()
    conn.close()