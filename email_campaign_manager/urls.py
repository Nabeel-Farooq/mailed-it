"""
URL configuration for the email_campaign_manager project.

The ``urlpatterns`` list routes URLs to views.

For more information, see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from __future__ import annotations

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
]
