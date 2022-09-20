from django.urls import include, path
from rest_framework import routers
from  .views import CustomUsersViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', CustomUsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
