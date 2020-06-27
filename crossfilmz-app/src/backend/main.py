from flask import Flask, render_template
from movie import Movie

app = Flask(__name__)

# Routing! Whatever app.route() contains is the href of a link, the end of the URL.


@app.route('/')
def main_page():
    return movie.query.all()


@app.route('/test')
def test():
    return "test"


# For local testing
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
