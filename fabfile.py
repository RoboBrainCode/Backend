from fabric.api import env, local, settings, run

def test():
  env.host_string = 'ec2-54-218-20-10.us-west-2.compute.amazonaws.com'
  env.user = 'deedy'
  env.key_filename = 'conf/www.pem'

def deploy():
  run('cd /var/www')
  run('git checkout master')
  run('git pull')
  run('sudo uwsgi --reload /tmp/robobrain-master.pid')

# def deploy():
  local('git checkout master')
  local('git pull')
  local('sudo uwsgi --reload /tmp/robobrain-master.pid')

