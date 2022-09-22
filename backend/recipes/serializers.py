from cgitb import lookup
from dataclasses import fields
from urllib import request
from rest_framework import serializers
import base64
from django.core.files.base import ContentFile
from django.db import transaction
from tags.models import Tags
from .models import Recipes
from tags.serializers import TagsSerializer

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')  
            ext = format.split('/')[-1]  
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)

class RecipesSerializer(serializers.ModelSerializer):
    
    image = Base64ImageField(required=False, allow_null=True)
    class Meta:
        fields = '__all__'
        model = Recipes
