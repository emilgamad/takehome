from .models import Topic, BlogPost
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework import filters
from .serializers import BlogPostSerializer,TopicSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter

class TopicFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Topic
        fields = ['title']

class TopicView(ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TopicFilter

class TopicDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author__username', lookup_expr='icontains')
    topic = CharFilter(field_name='topic__title', lookup_expr='icontains')

    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'topic']

class BlogPostsView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogPostFilter

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class APIRootView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'topics': reverse('topic-list', request=request),
            'blogposts': reverse('blogpost-list', request=request),
        })
    