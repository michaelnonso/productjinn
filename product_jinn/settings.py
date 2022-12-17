
"""
Django settings for product_jinn project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
os.environ['GDAL_LIBRARY_PATH'] = 'C:\\Users\\michael.ejeagba\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\osgeo\\gdal304'
os.environ['GEOS_LIBRARY_PATH'] = 'C:\\Users\\michael.ejeagba\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\osgeo\\geos_c.dll'
# os.environ['SPATIALITE_LIBRARY_PATH'] = 'C:\\Users\\michael.ejeagba\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\mod_spatialite-5.0.1-win-x86\\mod_spatialite.dll'
os.environ['PROJ_LIB'] = 'C:\\Users\\michael.ejeagba\\AppData\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\osgeo\\data\\proj'

#C:\Users\michael.ejeagba\AppData\Local\Programs\Python\Python310\Lib\site-packages\osgeo\data\\proj

GEOS_LIBRARY_PATH =os.environ['GEOS_LIBRARY_PATH']
GDAL_LIBRARY_PATH = os.environ['GDAL_LIBRARY_PATH']

# SPATIALITE_LIBRARY_PATH = os.environ['SPATIALITE_LIBRARY_PATH']


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0xofawo%j9%0pdmf$_d9ulqh8-)s8e)0!8^smsvf#6#4%g&gw8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product_jinn_app',
    'django.contrib.gis', #needed for geodjango
    'phonenumber_field',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters', # only works with generic API views
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'product_jinn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'product_jinn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# #USING SPATIALITE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.spatialite',
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# #USING POSGRESQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'productjinndb', 
#         'USER': 'entryway', 
#         'PASSWORD': 'entryway',
#         'HOST': '127.0.0.1', 
#         'PORT': '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'productjinndb', 
        'USER': 'entryway', 
        'PASSWORD': 'entryway',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}

POSTGIS_VERSION = (2, 0, 3)



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#for handling of images
import os

# Actual directory user files go to
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'mediafiles')

# URL used to access the media
MEDIA_URL = '/media/'

print(MEDIA_ROOT)
