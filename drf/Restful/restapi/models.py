from os import name
import os
from django.db import models
from django.contrib.auth.models import User, auth
from django.db.models.deletion import CASCADE
from .validators import validate_file_extension,file_size
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    filetype = models.FileField(validators=[validate_file_extension,file_size], upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.username + self.name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)