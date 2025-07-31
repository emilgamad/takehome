
"""
WSGI config for segstream_project project.

Exposes the WSGI callable as a module-level variable named ``application``.
For more information, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'segstream_project.settings')

application = get_wsgi_application()
