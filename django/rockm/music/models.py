from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Singer(models.Model):
	"""
	Model for Singer for a music
	"""
	name  = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Album(models.Model):
	"""
	Model for albums with one to many relation with songs
	"""
	# song = models.ForeignKey(Song, on_delete=models.CASCADE)
	album_name = models.CharField(max_length=200)
	release_date = models.DateField('release date')

	def __str__(self):
		return self.album_name


class Song(models.Model):
	"""
	Song Model for songs
	Many to many relation with singer
	"""

	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	song_name = models.CharField(max_length=300)
	# song_genre = models.CharField(max_length=200)
	song_length = models.DecimalField(max_digits=4, decimal_places=2)
	singer = models.ManyToManyField(Singer)

	def __str__(self):
		return self.song_name
