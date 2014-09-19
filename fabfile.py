from fabric.api import cd, env, local, settings, run, sudo

def prod():
  env.host_string = 'ec2-54-218-14-187.us-west-2.compute.amazonaws.com'
  env.key_filename = 'conf/www.pem'

def test():
  env.host_string = 'ec2-54-218-20-10.us-west-2.compute.amazonaws.com'
  env.key_filename = 'conf/www.pem'

def deploy(user='ubuntu'):
  env.user = user
  with cd('/var/www/Backend'):
    run('git checkout master')
    run('git pull')
    sudo('uwsgi --reload /tmp/robobrain-master.pid')
