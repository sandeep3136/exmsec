"""
ASGI config for internalapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internalapp.settings')

application = get_asgi_application()

import socket
# socket.getaddrinfo('localhost', 8080)

socket.getaddrinfo('localhost', 25)