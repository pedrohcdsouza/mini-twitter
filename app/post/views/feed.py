from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import Post
from ..serializers import PostSerializer
from ..pagination import FeedPagination
from users.models import Follow
from rest_framework.exceptions import PermissionDenied


class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = FeedPagination

    def get_queryset(self):
        user = self.request.user
        followed_users = Follow.objects.filter(following=user).values_list('followed', flat=True)
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')