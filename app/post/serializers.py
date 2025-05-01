from rest_framework import serializers
from .models import Post, Like

# This serializer is used to convert the Post model instances into JSON format and vice versa.

class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'created_at', 'updated_at']

# This serializer is used to convert the Like model instances into JSON format and vice versa.

class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Like
        fields = ['id', 'author', 'post', 'created_at']
        read_only_fields = ['author', 'created_at']