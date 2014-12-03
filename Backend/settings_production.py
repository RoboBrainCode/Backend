from settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'backend_test_deploy',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': 'ec2-54-148-208-139.us-west-2.compute.amazonaws.com',# Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '27017',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
	'.robobrain.me',
	'.robobrain.me.',
	'.127.0.0.1',
	'*'
]

