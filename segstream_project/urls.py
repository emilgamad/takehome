
"""
URL configuration for the segstream_project project.
Routes admin and blog app URLs to their respective views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
