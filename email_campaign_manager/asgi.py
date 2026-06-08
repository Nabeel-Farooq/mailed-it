"""
ASGI configuration for the email_campaign_manager project.

Exposes the ASGI application callable as a module-level variable named
``application``.

For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

from __future__ import annotations

import os

from django.core.asgi import get_asgi_application

# Default Django settings module for ASGI servers.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "email_campaign_manager.settings",
)

# ASGI application used by servers such as Uvicorn, Daphne, or Hypercorn.
application = get_asgi_application()
