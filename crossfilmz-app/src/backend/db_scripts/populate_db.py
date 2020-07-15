from movie import Movie
import db_ops
import sqlite3
import json
import requests


def get_availability(imdb_id):
    url = 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/idlookup'

    querystring = {
        'country': 'US',
        'source_id': imdb_id,
        'source': 'imdb'
    }

    headers = {
        'x-rapidapi-host': 'utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com',
        'x-rapidapi-key': # 'ifthereare1000+requestsonmykeytheychargemycreditcard'
    }

    response = requests.request("GET", url, headers=headers,
                                params=querystring).json()
    return response

def get_tags(movie):
    api_key = 'ed7bc645'
    url = ('http://www.omdbapi.com/?apikey={}'.format(api_key))
    params = {
        't': movie
    }

    response = requests.get(url, params=params).json()
    return response

def main():
    with open('sample_movies.txt') as f:
        movies = [line.rstrip('\n') for line in f]

    for movie in movies:
        conn, cur = db_ops.open_db_conn()
        omdb_info = get_tags(movie)
        tags = omdb_info['Genre']

        utelly_info = get_availability(omdb_info['imdbID'])

        availability = []
        for location in utelly_info['collection']['locations']:
            availability.append(location['display_name'])
        availability = str(availability).strip('[]')

        sql_command = """
            SELECT *
            FROM movies
            WHERE title = ?"""
        cur.execute(sql_command, (movie,))

        if cur.fetchone() is None:
            sql_command = """
                INSERT INTO movies
                (title, tags, availability)
                VALUES (?, ?, ?)"""
            cur.execute(sql_command, (movie, tags, availability,))

        db_ops.close_db_conn(conn)

if __name__ == "__main__":
    main()