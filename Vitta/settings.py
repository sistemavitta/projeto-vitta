# -*- coding: utf-8 -*-
"""
Django settings for Vitta project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h77t50*%1)lg_5r*=#@!85)(%c^&0i@xc(d2koluik(tpfb+=)'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
TEMPLATE_DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Allow all host headers
ALLOWED_HOSTS = ['*']

# Administradores do sistema
############
# SESSIONS #
############

SESSION_CACHE_ALIAS = 'default'                         # Cache to store session data if using the cache session backend.
SESSION_COOKIE_NAME = 'sessionid'                       # Cookie name. This can be whatever you want.
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2               # Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_DOMAIN = None                            # A string like ".example.com", or None for standard domain cookie.
SESSION_COOKIE_SECURE = True                           # Whether the session cookie should be secure (https:// only).
SESSION_COOKIE_PATH = '/'                               # The path of the session cookie.
SESSION_COOKIE_HTTPONLY = True                          # Whether to use the non-RFC standard httpOnly flag (IE, FF3+, others)
SESSION_SAVE_EVERY_REQUEST = False                      # Whether to save the session data on every request.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True                 # Whether a user's session cookie expires when the Web browser is closed.
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # The module to store session data
SESSION_FILE_PATH = None                                # Directory to store session files if using the file session module. If None, the backend will use a sensible default.
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'  # class to serialize session data

#########
# CACHE #
#########

# The cache backends to use.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = 'default'

ADMINS = (
    (u'bruce_alex2006@hotmail.com'),
    (u'william-urias@hotmail.com'),
)

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administration',
    'perfil',
    'training',

    'talks',
    'rest_framework',
    'south',
    'pyuploadcare.dj',
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Vitta.urls'

WSGI_APPLICATION = 'Vitta.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# Banco de dados local


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES= {
    'default': dj_database_url.config(default='postgres://localhost')
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

#TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"

MEDIA_ROOT =os.path.join(BASE_DIR,'Vitta/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"

MEDIA_URL = '/media/'



# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

STATIC_ROOT = os.path.join(BASE_DIR,'Vitta/staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'Vitta/static'),
)







# List of finder classes that know how to find static files in
# various locations.

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'administration.context_processors.context_fichas',
    'administration.context_processors.resolve_urlname',
)

UPLOADCARE = {
    'pub_key': '4d196208cb0bb2bef1e6',
    'secret': '3ddfcb1f3cc197ff4b0d',
    'widget_version': '0.18.3',
}


LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/perfil/%s/" % u.pk
}


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 20,
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 300,             # Maximum limit allowed when using `?page_size=xxx`.
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S' , #%a %d/%m/%Y %H:%M  -- '%a %x %X %z'
    #'DATETIME_INPUT_FORMATS' : '%d/%m/%Y %H:%M',
    # 'DATE_FORMAT': '%d/%m/%Y ',
    # 'DATE_INPUT_FORMATS' : '%d/%m/%Y ',
    # 'TIME_FORMAT' : '%H:%M:%S',

    # Coloquei aqui, mas são os defaults
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
        # poderia adicionar aqui por exemplo, o oauth2:
        # 'rest_framework.authentication.OAuth2Authentication'
    ),
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.YAMLParser',
    # ),

    # 'DEFAULT_PAGINATION_SERIALIZER_CLASS':
    #     'talks.serializers.CustomPaginationSerializer',
}

try:
    from settings_local import *
except ImportError:
    pass
