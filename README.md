# Django Rest Framework

How to implement a REST API using Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python, Django and a virtual environment to be installed


```
>> mkdir django

>> cd django

>> virtualenv venv

>> .\venv\Scripts\activate

>> pip install django

```

### Installing

Install the django REST Framework package

```
>> pip install djangorestframework
```

Create a django Project

```
>> django-admin startproject projects
```

Create the application /api
```
>> django-admin startapp api
```

Modify the file django/projects/projects/settings.py and add 2 lines into the INSTALLED_APPS section
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]
```

## Version 1.0 Tutorial

1. Modify thr file django/projects/api/models.py and create a new model Employee

2. Generate a new migration log file for the database structure based on the new model
```
>> py manage.py makemigrations
```

3. Migrate the DB changes based on the migration log file previously created
```
>> py manage.py migrate
```

4. Create the Administrator user in order to access the admin console
```
>> py manage.py createsuperuser --email admin@mail.com --username admin
```

5. Modify the file django/projects/api/admin.py and register the new model Employee in order to be visible through the admin console

6. Create a new file serializers.py in django/projects/api/
	 The serializer will follow the naming convention <name of the class model>Serializer

7. Modify the file django/projects/api/views.py add a view for the new model Employee
   The view will follow the naming convention <name of the class model>List

8. Modify the file django/projects/projects/urls.py and add a route for the new end point Employee

9. Test ypur application
```
>> py manage.py runserver
```

## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) - Python IDE

## Authors

* **Olivier A** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
