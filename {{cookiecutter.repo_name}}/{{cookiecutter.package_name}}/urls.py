from django.conf import settings
from django.contrib import admin
from django.urls import include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    re_path(r"^$", TemplateView.as_view(template_name="home.html"), name="home"),
    re_path(
        r"^accounts/",
        include("{{cookiecutter.package_name}}.users.urls", namespace="users"),
    ),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    # Render statics/media locally
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Do explicit setup of django debug toolbar
    import debug_toolbar

    urlpatterns += [re_path(r"^__debug__/", include(debug_toolbar.urls))]
