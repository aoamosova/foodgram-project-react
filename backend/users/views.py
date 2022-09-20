from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import User
from .serializers import CustomUserSerializer
class CustomUsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer