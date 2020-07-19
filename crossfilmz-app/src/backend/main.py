from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from movie import Movie
from flask_cors import CORS


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


# Routing! Whatever app.route() contains is the href of a link, the end of the URL.
@app.route('/')
@login_required
def hello_world():
    email = dict(session)['profile']['email']
    return f'Hello, you are logge in as {email}!'


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
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    session['profile'] = user_info
    # make the session permanant so it keeps existing after broweser gets closed
    session.permanent = True
    return redirect('/')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    user = User(user_data['login'])
    user_map[user_data['login']] = user
    return 'Done', 201


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

    return jsonify(Movie.select_all_movies())
    # return Movie.select_all_movies(), 'Done', '201'


@app.route('/add_rating', methods=['GET'])
# Could also just pass the entire movie object here if that's possible
# If so, there wouldn't be a need for the movie map
def add_rating(user_login, movie_title, score):
    user = user_map[user_login]
    movie = movie_map[movie_title]
    user.add_rating(movie, score)

    return 'Done', 201


@app.route('/get_recs', methods=['GET'])
def get_recs(user_login):
    user = user_map(user_login)
    user_recs = user.get_recs()

    return jsonify(user_recs)


@app.route('/filter_recs', methods=['GET'])
def filter_recs(user_login, platforms):
    for platform in platforms:
        if platform not in valid_platforms:
            return 'Invalid Platform', 500

    user = user_map(user_login)
    user_recs = user.get_recs()
    filtered_recs = user.filter_recs(user_recs, platforms)

    return jsonify(filtered_recs)


# For local testing
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
