from __future__ import with_statement
from fabric.api import cd, env, local, settings, run, sudo
from fabric.colors import green, red
from fabric.contrib.console import confirm

def prod_deploy(user='ubuntu'):
  print(red('Deploying to production at robobrain.me...'))
  if not confirm('Are you sure you want to deploy to production?'):
     print(red('Aborting deploy.'))
  env.host_string = '54.149.21.165'
  env.key_filename = 'conf/www.pem'
  env.user = user
  env.shell = '/bin/zsh -l -c'
  with cd('/var/www/Backend'):
    # sudo('su - ubuntu')
    print(green('Checking out test...'))
    run('git checkout test')
    print(green('Pulling latest version of test...'))
    run('git pull origin test')
    print(green('Checking out production...'))
    run('git checkout production')
    print(green('Rebasing onto test...'))
    run('git rebase test')
    print(green('Pushing production upstream...'))
    run('git push origin production')
    print(green('Reloading server...'))
    sudo('uwsgi --reload /tmp/robobrain-master.pid')
  print(red('Done!'))

def test_deploy(user='ubuntu'):
  env.host_string = 'ec2-54-148-225-192.us-west-2.compute.amazonaws.com'
  env.key_filename = 'conf/www.pem'
  env.user = user
  env.shell = '/bin/zsh -l -c'
  print(red('Deploying to test at test.robobrain.me...'))
  with cd('/var/www/Backend'):
    print(green('Checking out master...'))
    run('git checkout master')
    print(green('Pulling latest version of master...'))
    run('git pull origin master')
    print(green('Checking out test...'))
    run('git checkout test')
    print(green('Rebasing onto master...'))
    run('git rebase master')
    print(green('Pulling latest version of test...'))
    run('git pull origin test')
    print(green('Push the latest version of test...'))
    run('git push origin test')
    print(green('Reloading server...'))
    sudo('uwsgi --reload /tmp/robobrain-master.pid')
  print(red('Done!'))
