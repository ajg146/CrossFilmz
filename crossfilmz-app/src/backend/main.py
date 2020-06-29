from flask import Flask, render_template, request
from movie import Movie
app = Flask(__name__)

# Routing! Whatever app.route() contains is the href of a link, the end of the URL.


@app.route('/')
def main_page():
    return render_template("index.html", page_title="CrossFilmz")


@app.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    Movie(movie_data['title'],
          movie_data['genre'],
          movie_data['platform']
          )
    return 'Done', 201


@app.route('/get_movies', methods=['GET'])
def get_movies():
    Movie.select_all_movies()
    return 'Done', 201

    # For local testing
    if __name__ == "__main__":
    	app.run(host="127.0.0.1", port=8080, debug=True)
