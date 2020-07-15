from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from movie import Movie

app = Flask(__name__)

# Routing! Whatever app.route() contains is the href of a link, the end of the URL.


@app.route('/')
def main_page():
    return movie.query.all()


@app.route('/test')
def test():
    return "test"

@app.route('/get_movies', methods=['GET'])
def get_movies():
    movies = Movie.select_all_movies()
    return jsonify(movies)
    # return jsonify(title=movies[0], tags=movies[1], platforms=movies[2])

# For local testing
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
