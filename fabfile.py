from fabric.api import env, run, cd, local, sudo

APP_PATH = '/srv/www/hive.hivelocity.net/'

env.use_ssh_config = True
env.hosts = [
    'hive',
]


def deploy():
    test()
    push()
    restart()


def test():
    local('py.test')


def push():
    local('git push hive master')


def restart():
    sudo('/srv/restart.sh')
