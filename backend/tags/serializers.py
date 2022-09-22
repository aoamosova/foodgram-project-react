from cgitb import lookup
from dataclasses import fields
from rest_framework import serializers

from .models import Tags


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Tags
        lookup_fields = 'id'
        extra_kwargs = {'url':{'lookup_fields':'id'}}