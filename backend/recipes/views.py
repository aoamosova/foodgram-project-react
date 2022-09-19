from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import Recipes

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()

