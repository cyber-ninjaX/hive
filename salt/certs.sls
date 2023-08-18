{% for name, data in pillar.get('certs').items() %}

{% for extension in ['crt', 'key'] %}

/srv/ssl/{{ name }}.{{ extension }}:
  file.managed:
    - mode: 600
    - user: root
    - group: root
    - makedirs: true
    - dir_mode: 700
    - contents_pillar: certs:{{ name }}:{{ extension }}

{% endfor %}

{% endfor %}
