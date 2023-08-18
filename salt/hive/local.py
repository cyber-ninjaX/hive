"""Local settings."""

from .prod import *

DATABASES['default']['PASSWORD'] = '{{ pillar["postgres"]["password"] }}'
