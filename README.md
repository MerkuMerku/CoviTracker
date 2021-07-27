# CoviTracker

## Flask Setup

### Windows

#### Running the flask site - PRODUCTION

1. in the flask folder, navigate to the src directory
2. in powershell, run `$env:FLASK_APP = "flasksite.py"` to set the PATH variable for the flask application
3. run `python run_site.py` to start the site

#### Running the flask site - DEVELOPMENT

1. in the flask folder, navigate to the src directory
2. in powershell, run `$env:FLASK_APP = "flasksite.py"` to set the PATH variable for the flask application
3. in powershell, run `$env:FLASK_ENV = "development"` to switch to the development environment
4. run `python run_site.py` to start the site

### MacOS

#### Running the flask site - PRODUCTION

1. in the flask folder, navigate to the src directory
2. in zsh, run `export FLASK_APP = flasksite.py` to set the PATH variable for the flask application
3. run `python run_site.py` to start the site

#### Running the flask site - DEVELOPMENT

1. in the flask folder, navigate to the src directory
2. in zsh, run `export FLASK_APP = flasksite.py` to set the PATH variable for the flask application
3. in zsh, run `export FLASK_ENV = development` to switch to the development environment
4. run `python run_site.py` to start the site

## SQLite3

Open the site.db in sqlite3 with `sqlite3 site.db`
View tables using `.tables`
Once the database is open, SQL commands can be passed to the console. Remember to end statements with `;`
