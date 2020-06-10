from flask import Flask, render_template

app = Flask(__name__)

# Right now the login is the root page
# We might want to allow users access to the site without logging in
@app.route('/')
def main():
	return render_template("index.html", page_title="CrossFilmz")

@app.route("/login.html")
def login():
	return render_template("login.html", page_title="CrossFilmz Login")

# For local testing
if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)