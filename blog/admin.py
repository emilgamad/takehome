
"""
Admin configuration for the blog app, registering Author, Topic, and BlogPost models.
Customizes list display, search, and filtering in the Django admin interface.
"""
from django.contrib import admin
from .models import Author, Topic, BlogPost

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin configuration for Author model.
    """
    list_display = ('id', 'name', 'age')
    search_fields = ('name',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Admin configuration for Topic model.
    """
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin configuration for BlogPost model.
    """
    list_display = ('id', 'title', 'author', 'topic', 'publication_date')
    search_fields = ('title', 'content')
    list_filter = ('author', 'topic', 'publication_date')
