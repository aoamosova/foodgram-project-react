from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import Tags
from .serializers import TagsSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

