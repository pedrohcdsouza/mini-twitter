from rest_framework import serializers
from .models import Post

# This serializer is used to convert the Post model instances into JSON format and vice versa.

class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'created_at', 'updated_at']
