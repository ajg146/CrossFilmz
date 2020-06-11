# CrossFilmz
## Instructions for running local server
* Install Flask on machine: `pip install flask`
* Export `FLASK_APP` environment variable
  * Windows: `C:\path\to\app>set FLASK_APP=hello.py`
  * Powershell: `PS C:\path\to\app> $env:FLASK_APP = "hello.py"`
  * Linux: `export FLASK_APP=hello.py`
* Start server: `flask run` or `python -m flask run`

## Instructions for setting up and running testing frameworks
* Install pytest on machine: `pip install -U pytest`
* Check that pytest is version `5.x.y`: `pytest --version`
* Run tests using [standard test discovery rules](https://docs.pytest.org/en/stable/goodpractices.html#test-discovery): `pytest`
  * Note: tests will be run in current working directory and all subdirectories
