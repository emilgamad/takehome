
"""
Models for the blog app, including Author, Topic, and BlogPost.
Each model includes fields and string representations for use in the admin and API.
"""
from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Represents an author who writes blog posts.

    Attributes:
        name (CharField): The name of the author.
        age (PositiveIntegerField): The age of the author.
    """
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        """
        Returns the string representation of the author.

        Returns:
            str: The name of the author.
        """
        return self.name

class Topic(models.Model):
    """
    Represents a blog topic.

    Attributes:
        title (CharField): The title of the topic.
    """
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """
        Returns the string representation of the topic.

        Returns:
            str: The title of the topic.
        """
        return self.title

class BlogPost(models.Model):
    """
    Represents a blog post written by an author on a specific topic.

    Attributes:
        title (CharField): The title of the blog post.
        content (TextField): The content of the blog post.
        publication_date (DateTimeField): The date and time the blog post was published.
        author (ForeignKey): The author who wrote the blog post.
        topic (ForeignKey): The topic of the blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        """
        Returns the string representation of the blog post.

        Returns:
            str: The title of the blog post.
        """
        return self.title
