from fabric.api import cd, env, local, settings, run, sudo

def prod_deploy(user='ubuntu'):
  env.host_string = 'ec2-54-218-14-187.us-west-2.compute.amazonaws.com'
  env.key_filename = 'conf/www.pem'
  env.user = user
  with cd('/var/www/Backend'):
    run('git checkout test')
    run('git pull')
    run('git checkout production')
    run('git merge test')
    sudo('uwsgi --reload /tmp/robobrain-master.pid')

def test_deploy(user='ubuntu'):
  env.host_string = 'ec2-54-218-20-10.us-west-2.compute.amazonaws.com'
  env.key_filename = 'conf/www.pem'
  env.user = user
  with cd('/var/www/Backend'):
    run('git checkout master')
    run('git pull')
    run('git checkout test')
    run('git pull')
    run('git merge master')
    run('git push')
    sudo('uwsgi --reload /tmp/robobrain-master.pid')
