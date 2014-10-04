Backend
==============

### Setting up submodules
Once you pull or clone the Backend repo, you need to do:

1. `cd Backend/`

2. `git submodule init`

3. `git submodule update`


Any time a change to any of the submodules is pushed to the Backend repo, you
need to do `git submodule update`.

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

### Update viewer feeds

The script inside directory UpdateViewerFeeds runs as a cron job and balances the frontend feeds. Giving equal importance to all the projects. The script import the settings file mentioned in manage.py. So if you change the settings filename in manage.py, then accordingly modify the updateViewerFeed.py file. 
