from django.urls import path

from app import views


app_name = "app"

urlpatterns = [
    path("", views.main, name="home"),
    path("add-subscribe/", views.add_subscribe, name="add_subscribe"),
    path("unsubscribe/", views.unsubscribe, name="unsubscribe"),
    path("add-campaign/", views.add_campaign, name="add_campaign"),
    path("send-mail/", views.send_mail, name="send_mail"),
    path("success/", views.success_page, name="success_page"),
    path(
        "import-subscribers/",
        views.import_subscribers,
        name="import_subscribers",
    ),
    path(
        "user-unsubscribe/",
        views.user_unsubscribe,
        name="user_unsubscribe",
    ),
    path(
        "upload-template/",
        views.upload_template,
        name="upload_template",
    ),
]
