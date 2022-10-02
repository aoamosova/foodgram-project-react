from rest_framework import permissions, viewsets

from .models import Tags
from .serializers import TagsSerializer


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.AllowAny, ]
    pagination_class = None
