from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import Users

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()