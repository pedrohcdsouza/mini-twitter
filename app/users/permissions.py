from rest_framework.permissions import BasePermission

# Allow access only to the user themselves or if they are followed by the user

class IsSelfOrFollowed(BasePermission):
    def has_permission(self, request, view):
        username = view.kwargs.get('username')
        user = request.user
        if not user.is_authenticated:
            return False
        if username == user.username:
            return True
        return user.followed_by.filter(followed__username=username).exists()