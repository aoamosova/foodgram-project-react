from django.urls import include, path
from rest_framework import routers

from users.views import CustomUsersViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', CustomUsersViewSet, basename='users')

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
  