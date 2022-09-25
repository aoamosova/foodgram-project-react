from multiprocessing import context
from rest_framework import viewsets, permissions, response, status

from tags.views import TagsViewSet

from .models import Recipes
from .serializers import RecipesReadSerializer, RecipesCreateSerializer
from .permissions import IsAuthorOrReadOnly

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return RecipesReadSerializer
        return RecipesCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def create(self, request, *args, **Kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        instance = serializer.instance
        serializer = RecipesReadSerializer(
            instance=instance,
            context={'request': request}
        )
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
         )
