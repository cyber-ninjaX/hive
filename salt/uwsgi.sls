uwsgi-plugin-python:
  pkg:
    - installed

uwsgi:
  pkg:
    - installed
  service:
    - running
    - enable: True
    - watch:
      - file: /etc/uwsgi/apps-available/hive.hivelocity.net.json

/etc/uwsgi/apps-available/hive.hivelocity.net.json:
  file.managed:
    - source: salt://uwsgi/hive.hivelocity.net.json

/etc/uwsgi/apps-enabled/hive.hivelocity.net.json:
  file.symlink:
    - target: ../apps-available/hive.hivelocity.net.json
