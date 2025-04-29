from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Follow

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
    
class FollowSerializer(serializers.ModelSerializer):
    
    following = serializers.ReadOnlyField(source='following.username')
    followed = serializers.ReadOnlyField(source='followed.username')

    class Meta:

        model = Follow
        fields = ['following', 'followed', 'created_at']