from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from users.models import Subscriptions, User
from users.serializers import CustomUserSerializer, SubscriptionSerializer


class CustomUsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny, )

    @action(
        detail=False,
        methods=('get', ),
        permission_classes=(IsAuthenticated, )
    )
    def me(self, request):
        """users/me"""
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        permission_classes=(IsAuthenticated,)
    )
    def subscriptions(self, request):
        """Список на кого подписан пользователь."""
        user = request.user
        subscribed_authors = User.objects.filter(
            subscribed_authors__user=user
        ).order_by("subscribed_authors")
        pages = self.paginate_queryset(subscribed_authors)
        serializer = SubscriptionSerializer(
            pages,
            many=True,
            context={"request": request},
        )
        return self.get_paginated_response(serializer.data)

    @action(
        methods=('post', 'delete', ),
        detail=True,
        permission_classes=(IsAuthenticated,)
    )
    def subscribe(self, request, pk=None):
        """Подписаться/отписаться."""
        if request.method == "POST":
            user = request.user
            author = self.get_object()
            Subscriptions.objects.create(
                user=user,
                author=author,
            )
            serializer = SubscriptionSerializer(
                author,
                context={"request": request},
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == "DELETE":
            user = request.user
            author = self.get_object()
            subscription = Subscriptions.objects.filter(
                user=user,
                author=author,
            )
            if subscription.exists():
                subscription.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
