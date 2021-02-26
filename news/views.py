from rest_framework import permissions as p, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from news import services
from news.custom_permissions import IsOwnerOrAdmin
from news.models import Post, Comment
from news.serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permissions = [p.AllowAny]
        elif self.action in ["create", "vote", "unvote"]:
            permissions = [p.IsAuthenticated]
        else:
            permissions = [IsOwnerOrAdmin]
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(methods=["POST"], detail=True)
    def vote(self, request, pk=None):
        """
        This action to vote for Post object.
        """
        obj = self.get_object()
        services.add_vote(obj, request.user)
        serializer = PostSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["POST"], detail=True)
    def unvote(self, request, pk=None):
        """
        This action to delete vote for Post object.
        """
        obj = self.get_object()
        services.remove_vote(obj, request.user)
        serializer = PostSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permissions = [p.AllowAny]
        elif self.action == "create":
            permissions = [p.IsAuthenticated]
        else:
            permissions = [IsOwnerOrAdmin]
        return [permission() for permission in permissions]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
