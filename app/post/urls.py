from django.urls import path
from .views.post import PostCreateView, PostUpdateView, PostDeleteView, PostDetailView
from .views.feed import FeedView
from .views.like import LikeToggleView, LikeListView

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/likes/', LikeListView.as_view(), name='post-like-list'),
    path('post/like/<int:post_id>/', LikeToggleView.as_view(), name='post-like-toggle'),
    path('feed/', FeedView.as_view(), name='post-feed'),
]