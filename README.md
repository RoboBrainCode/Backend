Backend_django
==============

### Setup Django with MongoDB
* Follow the URL 

http://django-mongodb-engine.readthedocs.org/en/latest/topics/setup.html

* Execute the following commands:

1. sudo pip install git+https://github.com/django-nonrel/django@nonrel-1.5

2. sudo pip install git+https://github.com/django-nonrel/djangotoolbox

3. sudo pip install git+https://github.com/django-nonrel/mongodb-engine

4. sudo pip install djangorestframework


This will also install Django for you, further any Django project created will use MongoDB (and not the default sqlite3).

### Possible errors
* You might get an error (not necessarily) that DJANGO_SETTINGS_MODULE is not set. If this happens then follow the link

http://2buntu.com/articles/1451/installing-django-and-mongodb-in-your-virtualenv/

PS: There is no needs to setup virtualenv.
