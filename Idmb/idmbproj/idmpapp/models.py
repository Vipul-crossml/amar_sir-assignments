from django.db import models
# from django.forms import GENDER_CHOICES
from datetime import datetime
# Create your models here.

"""
choices for ratings
"""
RATING_CHOICE = [
    (1, '1 - Rubbish'),
    (2, '2 - Worst'),
    (3, '3 - Horrible'),
    (4, '4 - Bad'),
    (5, '5 - Below Average'),
    (6, '6 - Average'),
    (7, '7 - Nice'),
    (8, '8 - Awesome'),
    (9, '9 - Perfect'),
    (10, '10 - Mind blowing')
]
CATEGORY_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]
class Artist(models.Model):
    """
    class for storing artist info
    """
    name = models.CharField(max_length=30)
    dob = models.DateField(verbose_name='Date of birth')
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
    Date = models.DateField()

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
    Date = models.DateField()

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
    Release_date = models.DateField()
    Language = models.CharField(max_length=100)
    Artist = models.ManyToManyField(Artist)
    Length = models.DecimalField(max_digits=3, decimal_places=2)
    Awards_received = models.ManyToManyField(Award, null=True)
    avg_rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        """
        String representation for the class on DB
        """
        return self.name


class Rating(models.Model):
    """
    class for storing rating info
    """
    rating = models.IntegerField(choices=RATING_CHOICE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.__str__
