# hf-test

to run locally

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

To run using docker compose

change directory to hf-test/app

```
docker compose up

```
