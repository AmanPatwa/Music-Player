from django.db import models
from django.urls import reverse

class Album(models.Model):
    artist = models.CharField(max_length = 300)
    album_title = models.CharField(max_length = 300)
    genre = models.CharField(max_length = 100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 20)
    song_title = models.CharField(max_length = 300)
    is_favourite = models.BooleanField(default = False)
    audio_file = models.FileField(default = './media/1561360576060.jpg')

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.album.pk})

    def __str__(self):
        return self.song_title