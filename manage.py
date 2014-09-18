#!/usr/bin/env python
import os
import sys
import uwsgi
from uwsgidecorators import timer
from django.utils import autoreload

@timer(3)
def change_code_gracefull_reload(sig):
    if autoreload.code_changed():
	 uwsgi.reload()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Backend_django.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
