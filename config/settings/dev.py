from .base import *

SECRET_KEY = env("SECRET_KEY")

# Set the app DEBUG level
DEBUG = env("DEBUG")

# Apps
BUILTIN_APPS += []

THIRDPARTY_APPS = ['rest_framework']

LOCAL_APPS = ["apps.users", "apps.common"]

INSTALLED_APPS = BUILTIN_APPS + THIRDPARTY_APPS + LOCAL_APPS

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
