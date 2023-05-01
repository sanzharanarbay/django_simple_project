from rest_framework import serializers
from django.core.files.storage import FileSystemStorage
from django.core.validators import FileExtensionValidator
from django.db.models import Count
import os
import uuid
from datetime import datetime


class FormSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    education = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    type = serializers.IntegerField(required=True)
    phone = serializers.CharField(required=True)
