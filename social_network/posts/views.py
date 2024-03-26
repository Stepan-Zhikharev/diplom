from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Comment, Like

from posts.serializers import PostSerializer, CommentSerializer, LikeSerializer

from posts.permissions import IsOwnerOrReadOnly


# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


