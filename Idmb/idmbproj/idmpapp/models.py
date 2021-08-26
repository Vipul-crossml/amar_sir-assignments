from django.db import models
# from django.forms import GENDER_CHOICES
from datetime import datetime
# Create your models here.

"""
choices for ratings
"""
RATING_CHOICE = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
]
CATEGORY_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
]
class Artist(models.Model):
    """
    class for storing artist info
    """
    name = models.CharField(max_length=30)
    dob = models.DateTimeField(verbose_name='Date of birth')
    gender = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    # Awards_received = models.ForeignKey(Awards, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name

class Award(models.Model):
    """
    class used for movie awards
    """
    name = models.CharField(max_length=50)
    created_at = models.DateField()

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name


class Movie(models.Model):
    """
    class for storing info about movies
    """
    name = models.CharField(max_length=50)
    Genre = models.CharField(max_length=100)
    Release_date = models.DateTimeField()
    Language = models.CharField(max_length=100)
    Artist = models.ManyToManyField(Artist, blank=True)
    Length = models.DecimalField(max_digits=3, decimal_places=2)
    Awards_received = models.ManyToManyField(Award, blank=True)
    avg_rating = models.DecimalField(default=0,max_digits=4, decimal_places=2)

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name


class Rating(models.Model):
    """
    class for storing rating info
    """
    rating = models.PositiveSmallIntegerField(default=1,choices=RATING_CHOICE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.__str__
