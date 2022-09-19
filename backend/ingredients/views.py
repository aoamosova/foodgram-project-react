from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import Ingredients

class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
