from django.urls import path
from .views.post import PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, PostLikeView
from .views.feed import FeedView

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/like/<int:pk>/', PostLikeView.as_view(), name='post-like'), 
    path('feed/', FeedView.as_view(), name='post-feed'),
]