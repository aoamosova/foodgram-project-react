from django.urls import include, path
from rest_framework import routers
from  .views import IngredientsViewSet

app_name = 'ingredients'

router = routers.DefaultRouter()
router.register('ingredients', IngredientsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]