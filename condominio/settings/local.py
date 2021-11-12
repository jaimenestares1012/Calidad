

from .base import *



DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'condominio4',
        'USER': 'jaime',
        'PASSWORD': 'jaimee123',
        'HOST': 'localhost',
        'PUERTO': 5432,

    }
}

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


