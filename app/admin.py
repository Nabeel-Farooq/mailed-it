from django.contrib import admin

from app.models import Campaign, Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("id",)
    search_fields = ("id",)
    ordering = ("id",)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("id",)
    search_fields = ("id",)
    ordering = ("id",)
