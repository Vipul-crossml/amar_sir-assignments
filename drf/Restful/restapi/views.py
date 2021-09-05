from .models import Document
import os
from django.db import models
from django.contrib.auth.models import User, auth
from django.db.models.deletion import CASCADE
from .validators import validate_file_extension,file_size
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import DocumentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

users = User.objects.all()
"""
this loop will generate token for new users 
"""

for user in users:
    token, created = Token.objects.get_or_create(user=user)
    print (user.username, token.key)

class DocumentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Document instances.
    """
    authentication_classes=([TokenAuthentication,])
    permission_classes=([IsAuthenticated,])
    serializer_class = DocumentSerializer
    def get_queryset(self, *args, **kwargs):
        return Document.objects.filter(user=self.request.user)