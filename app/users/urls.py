from django.urls import path
from .views.authentication import RegisterView
from .views.follow import FollowingListView, FollowedView, FollowToggleView
from .views.user import UserDetailView
from rest_framework_simplejwt.views import (  # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('<str:username>/', UserDetailView.as_view(), name='user-detail'),
    path('<str:username>/following/', FollowingListView.as_view(), name='following-list'),
    path('<str:username>/followed/', FollowedView.as_view(), name='followed-list'),
    path('follow/<str:username>/', FollowToggleView.as_view(), name='follow-toggle'),
]