from __future__ import annotations

from django.db import models


class Campaign(models.Model):
    subject = models.TextField(blank=True, null=True)
    preview_text = models.CharField(max_length=500, blank=True, null=True)
    article_url = models.URLField(max_length=200, blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)
    plain_text_content = models.TextField(blank=True, null=True)
    campaign_name = models.CharField(max_length=100, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    campaign_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ["-published_date", "campaign_name"]
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self) -> str:
        return self.campaign_name or f"Campaign #{self.pk}"


class Subscriber(models.Model):
    STATUS_SUBSCRIBED = "subscribed"
    STATUS_UNSUBSCRIBED = "unsubscribed"

    STATUS_CHOICES = (
        (STATUS_SUBSCRIBED, "Subscribed"),
        (STATUS_UNSUBSCRIBED, "Unsubscribed"),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)

    subscribed_date = models.DateField()
    unsubscribed_date = models.DateField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_SUBSCRIBED,
    )

    campaigns = models.ManyToManyField(
        Campaign,
        related_name="subscribers",
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"
