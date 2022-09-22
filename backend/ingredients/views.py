from rest_framework import viewsets

from .models import Ingredients
from .serializers import IngredientsSerializer

class IngredientsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    pagination_class = None
