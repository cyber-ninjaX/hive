#!/bin/bash

salt-call --local \
          --file-root="/srv/www/hive.hivelocity.net/salt" \
          --pillar-root="/srv/www/hive.hivelocity.net/pillar" \
          state.highstate

# these are needed since salt is broken on ubuntu 15.05
# see: https://github.com/saltstack/salt/issues/23122
service nginx restart
service uwsgi restart
