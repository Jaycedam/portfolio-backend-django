# Portfolio backend (Django)
Django backend for [portfolio-frontend](https://github.com/Jaycedam/portfolio-frontend). Used for API requests with Django REST framework and JWT authentication.

## Set up local enviroment

* Use a Python virtual enviroment (optional) [Python documentation](https://docs.python.org/3/library/venv.html)

* Install dependencies
```
python3 -m pip install -r requirements.txt
```

* Set up enviroment variables. Create .env file in the project folder and use the variables used in the ".env-template" file. Example:
```
# DATABASE
NAME=DBNAME
```

* Resolve Django migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```

* Create superuser
```
python3 manage.py createsuperuser
```

* Run server
```
python3 manage.py runserver
```

## API Doc
Soon.