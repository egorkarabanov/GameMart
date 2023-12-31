from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Like
from .serializers import LikeCreateDeleteSerializer, LikeListSerializer
from rest_framework.permissions import IsAuthenticated


class LikeViewSet(CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Like.objects.all()
    http_method_names = ['get', 'post', 'delete']
    lookup_field = "game__pk"

    def get_serializer_class(self):
        if self.action == "list":
            return LikeListSerializer
        else:
            return LikeCreateDeleteSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # @action(methods=['delete'], detail=False)
    # def delete(self, request):
    #     try:
    #         Like.objects.get(game__pk=self.request.data.get("game")).delete()
    #         return Response(status=status.HTTP_200_OK)
    #     except Like.DoesNotExist:
    #         return Response(
    #             {"detail": "Like does not exist for the given user and game."},
    #             status=status.HTTP_404_NOT_FOUND
    #         )
