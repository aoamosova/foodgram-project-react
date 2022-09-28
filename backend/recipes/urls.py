from django.urls import include, path
from rest_framework import routers

from .views import RecipesViewSet

app_name = 'recipes'

router = routers.DefaultRouter()
router.register('recipes', RecipesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
   