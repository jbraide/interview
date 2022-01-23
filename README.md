# Interview 

* URL Shortner REST API built with Django and Django Rest Framework

# Getting Setup

Project requirements

* [Python >= 3.0](https://docs.python.org/3)
* [Django == 3.2](https://docs.djangoproject.com/en/3.2/)


Running the Django Server

* activate the virtualenvironment and enter into the project folder

```sh 
    source venv/bin/activate && cd urlshortner
```

* start up the django server

```sh
    python manage.py runserver 0.0.0.0:7000
```

## Available Endpoints

The root for the application lives at 

```sh
    https://tier-interview.herokuapp.com
```

To create a new short Url

* paste or type the link in the form field at the above url 

> OR 

* use curl in the terminal to generate a new short url 

```sh
curl -d '{"original_url":"type your url starting with https:// or http://"}' -H 'Content-Type: application/json' https://tier-interview.herokuapp.com
```