from django.urls import include, path
from rest_framework import routers
from  .views import UsersViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('django.contrib.auth.urls')),
]
