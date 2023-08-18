"""Development settings."""

import os

from .base import *


##############
# PATH STUFF #
##############


####################
# GENERAL SETTINGS #
####################

DEBUG = False

# console email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


########
# APPS #
########

INSTALLED_APPS += (
    'django_extensions',
    #'debug_toolbar',
)


##############
# MIDDLEWARE #
##############

#MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#)


#############
# DATABASES #
#############

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'hive.db',
#    },
#}


#########
# CACHE #
#########


#################
# MESSAGE QUEUE #
#################


############
# SESSIONS #
############

SESSION_COOKIE_SECURE = True


##################
# AUTHENTICATION #
##################


###########
# LOGGING #
###########


########
# URLS #
########

#ROOT_URLCONF = 'hive.dev_urls'


#############
# TEMPLATES #
#############


##################
# STATIC / MEDIA #
##################


########################
# MISC DJANGO SETTINGS #
########################


#########################
# MISC PROJECT SETTINGS #
#########################

## django debug toolbar
#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS': False,
#}
#INTERNAL_IPS = ('127.0.0.1',)
