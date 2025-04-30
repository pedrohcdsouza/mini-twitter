from django.urls import path
from .views.authentication import RegisterView
from .views.follow import FollowingListView, FollowedView, FollowToggleView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<str:username>/following/', FollowingListView.as_view(), name='following-list'),
    path('<str:username>/followed/', FollowedView.as_view(), name='followed-list'),
    path('follow/<str:username>/', FollowToggleView.as_view(), name='follow-toggle'),
]