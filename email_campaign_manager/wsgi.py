"""
WSGI configuration for the email_campaign_manager project.

Exposes the WSGI application callable as a module-level variable named
``application``.

For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application

# Default Django settings module for the WSGI server.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "email_campaign_manager.settings",
)

# WSGI application used by production servers.
application = get_wsgi_application()

# Optional alias for platforms expecting ``app``.
app = application
