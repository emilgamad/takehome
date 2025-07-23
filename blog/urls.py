from django.urls import path
from . import views
from .views import BlogPostDetailView, TopicDetailView, BlogPostsView, TopicView, APIRootView

urlpatterns = [
    path('topics/', TopicView.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('blogposts/', BlogPostsView.as_view(), name='blogpost-list'),
    path('api/', APIRootView.as_view(), name='api-root'),
    path('blogposts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
]