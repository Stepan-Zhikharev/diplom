from rest_framework import serializers

from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    post = serializers
    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at', 'post']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'comments', 'likes_count']

