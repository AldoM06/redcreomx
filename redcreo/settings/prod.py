 from .base import *
 import os
 # SECURITY WARNING: don't run with debug turned on in production!
 DEBUG = False

 ALLOWED_HOSTS = ['*']

 # Database
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': get_secret('DB_NAME'),
         'USER': get_secret('USER'),
         'PASSWORD': get_secret('PASSWORD'),
         'HOST': 'localhost',
         'PORT': '5432',
     }
 }
 #

 STATIC_URL = '/static/'
 #STATICFILES_DIRS = [BASE_DIR.child('static')]
 if DEBUG:
     STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
 else:
     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
 MEDIA_URL = '/media/'
 MEDIA_ROOT = BASE_DIR.child('media')
