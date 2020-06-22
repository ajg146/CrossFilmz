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
        if score < MIN_SCORE or score > MAX_SCORE:
            return # Make this be a more informative exception

        if movie.title not in self.ratings:
            for tag in movie.tags:
                self.vector[tag] = (self.vector[tag] *
                                    self.rating_count + score) / \
                                    (self.rating_count + 1) \
                                    if tag in self.vector else score
            self.rating_count += 1
        else:
            previous_rating = self.ratings[movie.title]
            for tag in movie.tags:
                self.vector[tag] += (score - previous_rating) / \
                                    self.rating_count
        self.ratings[movie.title] = score

    def get_ratings(self):
        return self.ratings

    def get_recs(self):
        netflix_recs = {}
        hulu_recs = {}
        amazon_recs = {}
        disney_recs = {}
        # {'movie.title': user_score}

        conn, cur = db_ops.open_db_conn()
        sql_command = """
            SELECT * FROM movies"""
        cur.execute(sql_command)
        movies = cur.fetchall()
        db_ops.close_db_conn(conn)

        for movie in movies:
            movie_score = 0
            tags = movie[1]
            platforms = movie[2]

            for tag in tags:
                if tag in self.vector:
                    movie_score += self.vector[tag]
                else:
                    movie_score += 2.5

            # For platform in platforms, see if it makes the top 10 scores

        # When done check its availability and put it in the appropriate symbol tables
        # ----- Maybe have to use a hashmap or something to store everything
        return [netflix_recs, hulu_recs, amazon_recs, disney_recs]

    def __init__(self, login):
        self.login = login
        self.vector = {}
        self.ratings = {}
        self.rating_count = 0
        self.add_user_to_db()


def main():
    user = User('aep67')
    movie = Movie('testmovie', ['action', 'drama'])
    user.add_rating(movie, 2)
    movie2 = Movie('other', ['action', 'comedy'])
    user.add_rating(movie2, 5)
    user.add_rating(movie, 3)
    print(user.ratings)
    print(user.vector)
    user.get_recs()

if __name__ == "__main__":
    main()