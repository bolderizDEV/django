# django
A set of implementations in Python with Django Framework

1. virtualenv venv

2. .\venv\Scripts\activate

3. pip install django djangorestframework

4. django-admin startproject projects

5. django-admin startapp api

6. in django/projects/projects/settings.py add 2 lines in INSTALLED_APPS
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

7. in django/projects/api/models create model Employee

8. py manage.py makemigrations

9. py manage.py migrate

10 py manage.py createsuperuser --email admin@mail.com --username admin

11 in django/projects/api/admin 
	- register the model Employee in order to be visible in the admin console
