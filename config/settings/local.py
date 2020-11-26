from .base import *  # noqa
from .base import env

# GENERAL
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="UZOvBl8WAwxMjk3RFh4428casSBtMK7g0m2X0lc5bm4S5NJUxfkelzRDtcA4YHYe",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# CACHES
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)


# django-extensions
INSTALLED_APPS += ["django_extensions"]  # noqa F405
