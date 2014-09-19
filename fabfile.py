from fabric.api import local

def deploy():
  local('git checkout master')
  local('git pull')
  local('sudo uwsgi --reload /tmp/robobrain-master.pid')
