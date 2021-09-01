from os import name
import os
from django.db import models
from django.contrib.auth.models import User, auth
from django.db.models.deletion import CASCADE
from django.core.validators import FileExtensionValidator
class Document(models.Model):
    """
    this model will deal with all sort of fuctionality related to user document
    """
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(validators=[FileExtensionValidator(['pdf'])], upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + self.description

    