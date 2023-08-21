# band/models.py
from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/', blank=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='songs/')
    total_votes = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.title


class SongVote(models.Model):
    song_name = models.CharField(max_length=200)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.song_name
