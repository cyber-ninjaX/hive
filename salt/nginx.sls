nginx:
  pkg:
    - installed
  service:
    - running
    - enable: True
    - watch:
      - file: /etc/nginx/*

{% for file in [
    'mime.conf',
    'nginx.conf',
    'restrictions.conf',
    'ssl.conf',
    'ssl-hivelocity.net.conf',
] %}

/etc/nginx/{{ file }}:
  file.managed:
    - source: salt://nginx/{{ file }}

{% endfor %}

{% for dir in ['sites-enabled', 'sites-available', 'conf.d'] %}

/etc/nginx/{{ dir }}:
  file.absent

{% endfor %}
