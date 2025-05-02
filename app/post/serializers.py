from rest_framework import serializers
from .models import Post, Like

# This serializer is used to convert the Post model instances into JSON format and vice versa.

class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    like_count = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'like_count', 'created_at', 'updated_at']

# This serializer is used to convert the Like model instances into JSON format and vice versa.

class LikeSerializer(serializers.ModelSerializer):
    
    author = serializers.CharField(source='author.username')

    class Meta:

        model = Like
        fields = ['author', 'created_at']