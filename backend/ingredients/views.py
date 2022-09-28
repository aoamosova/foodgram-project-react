from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets

from .filter import IngredientSearchFilter
from .models import Ingredients
from .serializers import IngredientsSerializer


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = (permissions.AllowAny, )
    pagination_class = None
    filter_backends = (DjangoFilterBackend, )
    filterset_class = IngredientSearchFilter
    
