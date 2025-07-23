# blog/serializers.py
from rest_framework import serializers
from .models import BlogPost, Author, Topic
from django.contrib.auth import get_user_model
from django.db.models import Count



class AuthorSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name','age']

class TopicSerializer(serializers.ModelSerializer):
    top_authors = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'title', 'top_authors']

    def get_top_authors(self, obj):
        # Get authors and their blog post counts for this topic
        authors = (
            Author.objects
            .filter(blog_posts__topic=obj)
            .annotate(blog_posts_count=Count('blog_posts'))
            .order_by('-blog_posts_count')[:3]
        )
        return AuthorSummarySerializer(authors, many=True).data

class TopicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BlogPostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    topic = TopicDetailSerializer()
    other_topics_by_author = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'publication_date', 'author', 'topic', 'other_topics_by_author']

    def get_other_topics_by_author(self, obj):
        # Get all unique topics by the same author excluding the current topic
        author_posts = BlogPost.objects.filter(author=obj.author).exclude(id=obj.id)
        topics = Topic.objects.filter(blog_posts__in=author_posts).exclude(id=obj.topic.id).distinct()
        return TopicDetailSerializer(topics, many=True).data