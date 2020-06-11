# CrossFilmz
## Instructions for running local server
* Install Flask on machine: `pip install flask`
* Export `FLASK_APP` environment variable
  * Windows: `C:\path\to\app>set FLASK_APP=hello.py`
  * Powershell: `PS C:\path\to\app> $env:FLASK_APP = "hello.py"`
  * Linux: `export FLASK_APP=hello.py`
* Start server: `flask run` or `python -m flask run`
