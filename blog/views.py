
"""
Views for the blog app, providing API endpoints for topics and blog posts.
Includes filters and root API view.
"""

from .models import Topic, BlogPost
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework import filters
from .serializers import BlogPostSerializer, TopicSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter

class TopicFilter(FilterSet):
    """
    Filter for Topic model based on title (case-insensitive contains).
    """
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Topic
        fields = ['title']

class TopicView(ListAPIView):
    """
    API view to list all topics with filtering support.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TopicFilter

class TopicDetailView(RetrieveAPIView):
    """
    API view to retrieve details of a single blog post by topic.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostFilter(FilterSet):
    """
    Filter for BlogPost model based on title, author, and topic (case-insensitive contains).
    """
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author__username', lookup_expr='icontains')
    topic = CharFilter(field_name='topic__title', lookup_expr='icontains')

    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'topic']

class BlogPostsView(ListAPIView):
    """
    API view to list all blog posts with filtering support.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogPostFilter

class BlogPostDetailView(RetrieveAPIView):
    """
    API view to retrieve details of a single blog post.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class APIRootView(GenericAPIView):
    """
    API root view that provides links to topic and blog post endpoints.
    """
    def get(self, request, *args, **kwargs):
        """
        Handle GET request and return available API endpoints.
        """
        return Response({
            'topics': reverse('topic-list', request=request),
            'blogposts': reverse('blogpost-list', request=request),
        })
