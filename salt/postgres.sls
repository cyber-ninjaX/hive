postgresql:
  pkg.installed:
    - pkgs:
      - postgresql
      - postgresql-contrib
      - libpq-dev

hivelocity:
  postgres_user.present:
    - login: true
    - createdb: true
    - password: {{ pillar['postgres']['password'] }}

hive:
  postgres_database.present:
    - owner: hivelocity
