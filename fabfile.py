from __future__ import with_statement
from fabric.api import cd, env, local, settings, run, sudo
from fabric.colors import green, red
from fabric.contrib.console import confirm

def prod_deploy(user='ubuntu'):
  print(red('Deploying to production at robobrain.me...'))
  if not confirm('Are you sure you want to deploy to production?'):
     print(red('Aborting deploy.'))
  test_deploy(user)
  env.host_string = 'ec2-54-218-14-187.us-west-2.compute.amazonaws.com'
  env.key_filename = 'conf/www.pem'
  env.user = user
  with cd('/var/www/Backend'):
    print(green('Checking out test...'))
    run('git checkout test')
    print(green('Pulling latest version of test...'))
    run('git pull')
    print(green('Checking out production...'))
    run('git checkout production')
    print(green('Merging with test...'))
    run('git merge test')
    print(green('Reloading server...'))
    sudo('uwsgi --reload /tmp/robobrain-master.pid')
  print(red('Done!'))

def test_deploy(user='ubuntu'):
  env.host_string = 'ec2-54-218-20-10.us-west-2.compute.amazonaws.com'
  env.key_filename = 'conf/www.pem'
  env.user = user
  print(red('Deploying to test at test.robobrain.me...'))
  with cd('/var/www/Backend'):
    print(green('Checking out master...'))
    run('git checkout master')
    print(green('Pulling latest version of master...'))
    run('git pull')
    print(green('Checking out test...'))
    run('git checkout test')
    print(green('Pulling latest version of test...'))
    run('git pull')
    print(green('Merging with master...'))
    run('git merge master')
    print(green('Push the latest version of master...'))
    run('git push')
    print(green('Reloading server...'))
    sudo('uwsgi --reload /tmp/robobrain-master.pid')
  print(red('Done!'))
