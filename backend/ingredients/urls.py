from django.urls import include, path
from rest_framework import routers

from .views import IngredientsViewSet

app_name = 'ingredients'

router = routers.DefaultRouter()
router.register('ingredients', IngredientsViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
]
