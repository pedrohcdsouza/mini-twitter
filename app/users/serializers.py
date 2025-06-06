from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Follow


class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'followers_count']

    def get_followers_count(self, obj):
        return obj.followed.count()

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class FollowingSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source='following.username')
    following = serializers.CharField(source='followed.username')

    class Meta:
        model = Follow
        fields = ['user','following','created_at']

class FollowedSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source='following.username')
    followed = serializers.CharField(source='followed.username')

    class Meta:
        model = Follow
        fields = ['user','followed','created_at']
