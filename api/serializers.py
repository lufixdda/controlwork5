from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'body', 'created_at', 'updated_at', 'is_approved']
        read_only_fields = ['author', 'is_approved', 'created_at', 'updated_at', 'post']


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'author_username', 'title', 'body', 'created_at', 'updated_at', 'is_published']
        read_only_fields = ['author', 'created_at', 'updated_at']