# hf-test

## Running the server locally

at the root of the directy run

```
pipenv install
```

then change directory to hf-test/app/ and run

```
pipenv run python manage.py migrate
pipenv run python load_mock.py
pipenv run python runserver

```

The server should start running with port 8000 by default:
http://127.0.0.1:8000

Note that to add a game you might need to create the studio and platform first if they do not exist in the database.

Games can be filtered on their name, studio o
for example
http://127.0.0.1:8000/games/?search=nintendo

## Running the server using Docker compose

I started adding a docker compose file and modifying the django setting to run postgres but I run out of time

To run using docker compose

change directory to hf-test/app

```
docker compose up --build

```

you can see the swagger documentation at http://127.0.0.1:8080/ by running

```
docker compose up --build swagger
```
