from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models import Follow
from ..serializers import FollowingSerializer, FollowedSerializer

User = get_user_model()

# Class to handle the list of users that the authenticated user is following

class FollowingListView(ListAPIView):
    serializer_class = FollowingSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        return Follow.objects.filter(following__username=username)
    
# Class to handle the list of users that are following the authenticated user

class FollowedView(ListAPIView):

    serializer_class = FollowedSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        return Follow.objects.filter(followed__username=username)
    
# Class to handle the follow/unfollow functionality

class FollowToggleView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):

        try:

            followed = User.objects.get(username=username)

        except User.DoesNotExist:

            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user == followed:

            return Response({'detail': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        _, created = Follow.objects.get_or_create(following=request.user, followed=followed)

        if created:

            return Response({'detail': f'You are now following {followed.username}'}, status=status.HTTP_201_CREATED)
        
        else:

            return Response({'detail': f'You are already following {followed.username}'}, status=status.HTTP_200_OK)
        
    def delete(self, request, username):

        try:

            followed = User.objects.get(username=username)

        except User.DoesNotExist:

            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user == followed:

            return Response({'detail': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        deleted, _ = Follow.objects.filter(following=request.user, followed=followed).delete()

        if deleted:

            return Response({'detail': f'You have unfollowed {followed.username}'}, status=status.HTTP_204_NO_CONTENT)
        
        else:
            
            return Response({'detail': f'You are not following {followed.username}'}, status=status.HTTP_400_BAD_REQUEST)
