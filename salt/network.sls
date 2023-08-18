vlan:
  pkg.installed

/etc/network/interfaces:
  file.managed:
    - source: salt://network/interfaces
