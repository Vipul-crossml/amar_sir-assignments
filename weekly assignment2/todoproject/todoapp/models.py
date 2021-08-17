from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Task(models.Model):
    """
    Stores the Task name,status of the task,
    the time of the task when created.
    """
    name = models.CharField(max_length=200)
    #Boolean field is used to display the status of the task

    status = models.BooleanField(default=False)
    started = models.DateTimeField(auto_now_add=True)

    # function to return a string when query fetch the name object from DB
    def __str__(self):
        return self.name
