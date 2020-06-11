from flask import Flask, render_template

app = Flask(__name__)

# Routing! Whatever app.route() contains is the href of a link, the end of the URL.

@app.route('/')

def main():
	return render_template("index.html", page_title="CrossFilmz")

@app.route("/login")
def login():
	return render_template("login.html", page_title="CrossFilmz Login")

@app.route("/search")
def login():
	return render_template("search.html", page_title="CrossFilmz")

# For local testing
if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)