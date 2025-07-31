
"""
URL configuration for the blog app, mapping endpoints to views for topics and blog posts.
"""
from django.urls import path
from . import views
from .views import BlogPostDetailView, TopicDetailView, BlogPostsView, TopicView, APIRootView

urlpatterns = [
    # List all topics
    path('topics/', TopicView.as_view(), name='topic-list'),
    # Retrieve details for a specific topic
    path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    # List all blog posts
    path('blogposts/', BlogPostsView.as_view(), name='blogpost-list'),
    # API root endpoint
    path('api/', APIRootView.as_view(), name='api-root'),
    # Retrieve details for a specific blog post
    path('blogposts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
]