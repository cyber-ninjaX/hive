"""Base settings for all other environments."""

import os


##############
# PATH STUFF #
##############

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
REPO_PATH = os.path.dirname(PROJECT_PATH)
_rel = lambda *args: os.path.abspath(os.path.join(REPO_PATH, *args))


####################
# GENERAL SETTINGS #
####################

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["10.42.42.211"]

ADMINS = (
    ('Dev', 'dev@hivelocity.net'),
)
MANAGERS = ADMINS

# default email addresses
SERVER_EMAIL = 'no-reply@hivelocity.net'
DEFAULT_FROM_EMAIL = 'no-reply@hivelocity.net'


########
# APPS #
########

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # third party apps
    'reversion',
    'apps',
    'audit',
    'otp_login',
    'passwords',
    'django_fields'
)


##############
# MIDDLEWARE #
##############

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'audit.middleware.AuditEventMiddleware',
)


#############
# DATABASES #
#############

DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hive_hive',
        'USER': 'postgres',
	'PASSWORD': '',
	'HOST': '127.0.0.1',
	'PORT': '5432'
    }
}




#########
# CACHE #
#########


#################
# MESSAGE QUEUE #
#################


############
# SESSIONS #
############

# different cookie name for the hive
SESSION_COOKIE_NAME = 'sessionid-hive'

# session age
SESSION_COOKIE_AGE = 259200  # 3 days
SESSION_SAVE_EVERY_REQUEST = True  # save session to db and resend session
                                   # cookie on every request

# enable httponly for session cookies (default in django 1.4)
SESSION_COOKIE_HTTPONLY = True

# enable secure cookies
SESSION_COOKIE_SECURE = True


##################
# AUTHENTICATION #
##################


###########
# LOGGING #
###########

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'file': {
#            'level': 'ERROR',
#            'class': 'logging.FileHandler',
#            'filename': '/var/log/hive.hivelocity.net.log',
#        },
#    },
#    'loggers': {
#        'django.request': {
#            'handlers': ['file'],
#            'level': 'ERROR',
#            'propagate': True,
#        },
#    }
#}


########
# URLS #
########

ROOT_URLCONF = 'hive.urls'


#############
# TEMPLATES #
#############

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [_rel('templates') ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]


##################
# STATIC / MEDIA #
##################

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = _rel('public')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = _rel('static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


########################
# MISC DJANGO SETTINGS #
########################

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Make this unique, and don't share it with anybody.
# TODO might want to factor this out into local settings so it isn't in repo
SECRET_KEY = '8iv#v%5$lx89xiwdn+ai=+r#b8!1ke)rup*llaq0gkbs1g!sdn'


#########################
# MISC PROJECT SETTINGS #
#########################

YUBI_CLIENT_ID = 1
# XXX: if both URLs are used, the second always returns REPLAYED_OTP. Use one.
YUBI_API_URLS = ['http://172.31.0.241/wsapi/verify']
