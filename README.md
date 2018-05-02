# Organisation website

## Install pipenv

The project is setup to use [Pipenv](https://docs.pipenv.org/)

First install Pipenv:
```
pip install pipenv
```
Then use Pipenv to install dependencies
```
pipenv install
```
## Run development server
```
cd django/cc
pipenv run python manage.py runserver
```

## Run Gunicorn locally

Uncomment the static files url in urls.py
Then run using this command
```
gunicorn -c gunicorn.py cc.wsgi:application
```
