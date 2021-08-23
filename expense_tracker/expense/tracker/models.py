from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Expense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    category = models.CharField(max_length=266)
    # created_by = models.CharField(max_length=100)
    # created_at = models.DateField()

    class Meta:
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return self.category

 


class Category(models.Model):
    # name = models.CharField(max_length=255)
    # expense = models.ForeignKey(Expense,on_delete=CASCADE)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name