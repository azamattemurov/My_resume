from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class Song(models.Model):
    song_name = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=200)
    album_thumbnail = models.ImageField(upload_to='album_thumbnails/')
    audio_file = models.FileField(upload_to='songs/')
    download_count = models.IntegerField(default=0)
    AUTH_USER_MODEL = 'auth.User'

    def __str__(self):
        return self.song_name
