import db_ops
import sqlite3


def main():
    conn, cur = db_ops.open_db_conn()

    # For testing out the script
    # (have to create a test table called testmovies)
    # sql_command = """
    #     INSERT INTO testmovies
    #     (title, tags)
    #     VALUES (?, ?)"""
    # cur.execute(sql_command, ('Title', 'Tag1, Tag2'))

    sql_command = """
        SELECT *
        FROM movies"""
    cur.execute(sql_command)
    table = cur.fetchall()

    sql_command = """
        UPDATE movies
        SET tags = ?
        WHERE title = ?"""

    for row in table:
        li = row[1].split(', ')
        li = str(li).strip('[]')
        print(li)
        cur.execute(sql_command, (li, row[0]))

    db_ops.close_db_conn(conn)

if __name__ == "__main__":
    main()
