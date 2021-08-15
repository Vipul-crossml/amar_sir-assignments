from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    started = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name
