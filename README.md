# django-todo

Code Along With Dennis Ivy's "Django To Do List With User Registration &amp; Login"

## Common Commands

$ python -m venv .venv
$ source .venv/bin/activate
$ pip install django

$ django-admin startproject <project name>
$ python manage.py startapp <app name>
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver

## Order

1. register app in project settings.py <name>..apps.BaseConfig
2. connect app's urls.py to project's urls.py
3. views.py: proof of life return HttpResponse("To Do List") on home route
4. link views to app's urls.py
5. 2 step migrations
6. register db with django admin panel - <app name>'s admin.py
from .models import <Model>
admin.site.register(<Model>)
7. switch to class base view in views.py, inherits from ListView
import model
8. urls.py import and <Model>.as_view()
9. create templates folder in app
inside folder, another folder with app name
<model name>_list.html (check get error)
10. for task in object_list: 
    {{task.title}}
use {% %}
render in table
11. context_object_name = 'tasks' in views, change object_list to new name in html
12. add detail view in views
13. in templates/<app>, add task_detail.html
context_object_name, change html