from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title
