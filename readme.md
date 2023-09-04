# Codecool Series

## About the project

This project was part of the web module curriculum at [Codecool](https://codecool.com) (a full-stack development bootcamp).

The website can be used to explore and discover TV series. Codecool provided a pre-designed interface and a database sourced from trakt.tv. The primary goal was to connect the dots and present the data in a user-friendly manner.

## Technologies

- PostgreSQL queries with SELECT, WHERE, JOIN, GROUP BY, ORDER BY, LIMIT, OFFSET and aggregate functions
- Flask routes and variable rules
- Jinja2 templating
- basic HTML tags
- some JavaScript
- basic algorhitmic and formatting topics

## Setup of database & virtual environment

**Clone the project:**

```
git clone git@github.com:zerqatu/codecool-series.git
```

**Create a PostgreSQL database:**

```
createdb zerqatu-codecool-series
```

**Add database info:**

Rename `.env.template` to `.env` and fill in the following details:

- MY_PSQL_DBNAME – The name of the database to be filled with the movie data
- MY_PSQL_USER – The database to be used for creating data
- MY_PSQL_HOST – localhost
- MY_PSQL_PASSWORD – The database user password. If no password is needed, put a random word here
- TRAKT_API_KEY – You can leave this empty

**Create the virtual environment, install requirements, fill database:**

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.tx
python3 data/data_inserter.py
```

## Running the site

```
source venv/bin/activate
python3 main.py
```

The site will run on [127.0.0.1:5000](http://127.0.0.1:5000) by default.

## Screenshots

**Index page:**

![screenshot1_index](https://github.com/zerqatu/codecool-series/assets/97981029/c4434cc2-fdbf-4b4d-be0f-78f016286840)

**List of highest rated shows:**

![screenshot2_shows](https://github.com/zerqatu/codecool-series/assets/97981029/0bab9143-007a-4aa6-b6b1-9bcd0f39e6a2)

**Detail view:**

![screenshot3_details](https://github.com/zerqatu/codecool-series/assets/97981029/a0fa1753-28af-46d6-a2a3-7b18f3d511d7)

**Ordered shows:**

![screenshot4_ordered_shows](https://github.com/zerqatu/codecool-series/assets/97981029/427135ff-6246-4f69-9293-18bb43f005de)

**Oldest actors:**

![screenshot5_oldest_actors](https://github.com/zerqatu/codecool-series/assets/97981029/1c00ebd9-a689-4cdf-8509-abbf13663b10)
