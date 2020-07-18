import db_ops
import sqlite3
import requests
import json

url = 'http://www.omdbapi.com/?&apikey=c8fb5dde'

query_string = {
    't': ''
}

def main():
    conn, cur = db_ops.open_db_conn()

    sql_command = """
        SELECT *
        FROM movies"""
    cur.execute(sql_command)
    table = cur.fetchall()

    for row in table:
        sql_command = """
            UPDATE movies
            SET poster = ?
            WHERE title = ?"""

        query_string['t'] = row[0]
        response = requests.request('GET', url, params=query_string)
        results = response.json()

        if results['Response'] == 'False':
            continue

        poster = results['Poster']
        cur.execute(sql_command, (poster, row[0]))

    db_ops.close_db_conn(conn)

if __name__ == "__main__":
    main()