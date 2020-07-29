from flask import Flask, render_template, request, redirect, url_for, \
    session, jsonify
from movie import Movie
from flask_cors import CORS, cross_origin
from user import User

from authlib.integrations.flask_client import OAuth
import os
from datetime import timedelta

# decorator for routes that should be accessible only by logged in users
from auth_decorator import login_required

# dotenv setup
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Session config
app.secret_key = os.getenv("APP_SECRET_KEY")
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    # This is only needed if using openId to fetch user info
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)


user_map = {}
movie_map = {}
valid_platforms = ['Netflix', 'Hulu', 'Amazon Instant Video', 'Disney+']
user_email = ""


# Routing! Whatever app.route() contains is the href of a link,
# the end of the URL.
@app.route('/')
@login_required
def hello_world():
    email = dict(session)['profile']['email']
    return f'Hello, you are logged in as {email}!'


@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    # Access token from google (needed to get user info)
    token = google.authorize_access_token()
    # userinfo contains stuff u specificed in the scrope
    resp = google.get('userinfo')
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and
    # query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    # make the session permanant so it keeps existing
    # after broweser gets closed
    session.modified = True
    session.permanent = True

    email = dict(session)['profile']['email']
    if email not in user_map:
        add_user(email)

    return redirect("http://localhost:3000/", code=302)


@app.route('/logout', methods=['GET'])
@cross_origin(origin='*')
def logout():
    print("in logout method")
    for key in list(session.keys()):
        print("popping")
        session.pop(key)
    return redirect("/login", code=302)


def add_user(email):
    user = User(email)
    user_map[email] = user
    print('added user')
    return 'Done'


@app.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()
    movie = Movie(movie_data['title'], movie_data['genre'],
                  movie_data['platform'])
    movie_map[movie_data['title']] = movie
    return 'Done', 201


@app.route('/get_movies', methods=['GET', 'POST'])
def get_movies(platforms=None):
    # Filtering the grid (if we want to be able to do that)
    platforms = request.get_json()['platforms']
    if platforms is not None:
        return jsonify(Movie.select_some_movies(platforms))


@app.route('/get_rating', methods=['POST'])
def get_rating(title=None):
    user_email = 'samirsherlekar98@gmail.com'
    user = user_map[user_email]
    title = request.get_json()['title']

    if title is not None and title in user.ratings:
        print(user.ratings)
        return jsonify({'rating': user.ratings[title]})

    return jsonify({'rating': 0})  # movie has not been rated


@app.route('/add_rating', methods=['POST'])
def add_rating():
    user_email = 'samirsherlekar98@gmail.com'
    user = user_map[user_email]
    movie_data = request.get_json()
    # genre and score recieved as
    # ["'Amazon Instant Video', 'iTunes', 'Google Play', 'Hulu'"]
    tags = movie_data['genre'].replace("'", "").split(", ")
    platforms = movie_data['platform'].replace("'", "").split(", ")
    movie = Movie(movie_data['title'],
                  tags,
                  platforms)
    user.add_rating(movie, movie_data['score'])
    return jsonify('Done', 201)


@app.route('/get_user_ratings', methods=['GET'])
def get_user_ratings():
    user_email = 'samirsherlekar98@gmail.com'
    user = user_map[user_email]
    user_ratings = user.get_full_ratings()
    return jsonify(user_ratings)


@app.route('/get_recs', methods=['GET'])
def get_recs():
    user_email = 'samirsherlekar98@gmail.com'
    user = user_map[user_email]
    user_recs = user.get_recs()
    formatted_recs = user.format_recs(user_recs)
    return jsonify(formatted_recs)


@app.route('/filter_recs', methods=['POST'])
@cross_origin(origin='*')
def filter_recs():
    user_email = 'samirsherlekar98@gmail.com'
    user_platform = request.get_json()['platform']
    user = user_map[user_email]
    user_recs = user.get_recs()
    filtered_recs = user.filter_recs(user_recs, user_platform)
    formatted_recs = user.format_recs(filtered_recs)
    return jsonify(formatted_recs)


# For local testing
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
