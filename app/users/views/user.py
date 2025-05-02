from rest_framework import generics
from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserDetailView(generics.RetrieveAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]