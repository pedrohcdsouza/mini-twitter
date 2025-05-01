from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from ..serializers import LikeSerializer
from rest_framework import status, permissions
from ..models import Post, Like
from users.models import Follow
from rest_framework.exceptions import PermissionDenied


class LikeToggleView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):

        try:

            post = Post.objects.get(id=post_id)

        except Post.DoesNotExist:

            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        
        is_following = Follow.objects.filter(following=request.user, followed=post.author).exists()

        if not is_following:
            
            return Response({"error": "You must follow the author to like their post."}, status=status.HTTP_403_FORBIDDEN)
        
        like, created = Like.objects.get_or_create(author=request.user, post=post)

        if created:

            return Response({"message": "Post liked."}, status=status.HTTP_201_CREATED)
        
        else:

            like.delete()

            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)

class LikeListView(ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(post__id=self.kwargs['post_id']).order_by('-created_at')

        