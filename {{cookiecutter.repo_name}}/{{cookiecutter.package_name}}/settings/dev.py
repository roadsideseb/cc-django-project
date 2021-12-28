from .base import Base


class Dev(Base):
    DEBUG = True

    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INSTALLED_APPS = Base.INSTALLED_APPS + [
        "debug_toolbar.apps.DebugToolbarConfig",
    ]
    MIDDLEWARE_CLASSES = [
        "debug_toolbar.middleware.DebugToolbarMiddleware"
    ] + Base.MIDDLEWARE_CLASSES
    INTERNAL_IPS = ["127.0.0.1", "::1"]

    @property
    def TEMPLATES(self):
        Base.TEMPLATES[0]["OPTIONS"]["debug"] = True
        Base.TEMPLATES[0]["OPTIONS"]["loaders"] = (
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        )
        return Base.TEMPLATES  # Disable the cached template loading

    # We just want to see emails displayed in the console
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

    ALLOWED_HOSTS = ["*"]
