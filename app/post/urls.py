from django.urls import path
from .views.post import PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, PostListView
from .views.feed import FeedView
from .views.like import LikeToggleView, LikeListView

app_name = 'post'

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/like', LikeToggleView.as_view(), name='post-like-toggle'),
    path('<int:post_id>/likes/', LikeListView.as_view(), name='post-like-list'),
    path('feed/', FeedView.as_view(), name='post-feed'),
    path('', PostListView.as_view(), name='post-list'),
]