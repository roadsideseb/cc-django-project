from django.urls import re_path
from django.views.generic import TemplateView

app_name = "users"

urlpatterns = [
    re_path(
        r"^profile/$",
        TemplateView.as_view(template_name="users/profile.html"),
        name="profile",
    ),
]
