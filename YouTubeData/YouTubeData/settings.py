"""
Django settings for YouTubeData project.

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
SECRET_KEY = 'ng+7ya)972j+3u14i*@-v5x*mk=k6@bf4%f$mv6^2ud740sd#9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AppYouTubeData',
    'rest_framework',
    'rest_framework.authtoken',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'AppYouTubeData.backends.EmailAuthBackend',
)

ROOT_URLCONF = 'YouTubeData.urls'

WSGI_APPLICATION = 'YouTubeData.wsgi.application'

REST_FRAMEWORK = {

   'DEFAULT_MODEL_SERIALIZER_CLASS':
       'rest_framework.serializers.ModelSerializer',


   'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.AllowAny'
   ]
}

REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
               'rest_framework.authentication.TokenAuthentication',
               'rest_framework.authentication.SessionAuthentication'
   )
}
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_',
        'NAME': 'YouTube',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#
# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR,  'templates'),
# )

DEVELOPER_KEY = "AIzaSyARh_LD390wO9raTVp40HSIiv2l4Pn2yG4"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

LOGIN_URL = '/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\','/')
MEDIA_URL = '/media/'
LOCALE_PATHS = (os.path.join(os.path.dirname(__file__), '..', 'locale').replace('\\','/'),)
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)
STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'static').replace('\\','/'),)