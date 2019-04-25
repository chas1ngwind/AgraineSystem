from django.conf import settings
from storages.backends.ftp import FTPStorage

class StaticStorage(FTPStorage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(FTPStorage):
    location = settings.MEDIAFILES_LOCATION


