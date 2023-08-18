
/srv/www/hive.hivelocity.net/hive/settings/local.py:
  file.managed:
    - template: jinja
    - source: salt://hive/local.py


{# logging #}

/var/log/hive.hivelocity.net.log:
  file.managed:
    - mode: 0666


{# python deps #}

deps:
  cmd.run:
    - name: "pip install -r /srv/www/hive.hivelocity.net/reqs/prod.txt"
    - cwd: /usr/local/lib/python2.7/dist-packages
    - user: root
