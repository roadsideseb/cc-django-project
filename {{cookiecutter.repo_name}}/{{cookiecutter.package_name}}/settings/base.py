import os

from configurations import Configuration, values

from structlog import configure
from structlog.stdlib import LoggerFactory

from . import mixins


configure(logger_factory=LoggerFactory())


def project_path(*path):
    this_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(this_dir, "..", *path)


class Base(mixins.DjangoLoggingMixin, Configuration):
    DEBUG = False

    ADMINS = (("Alerts", "{{cookiecutter.repo_name}}@{{ cookiecutter.domain }}"),)
    MANAGERS = ADMINS

    AUTH_USER_MODEL = "users.User"

    CACHES = values.CacheURLValue("locmem:///")

    DATABASE_DICT = values.DatabaseURLValue()

    @property
    def DATABASES(self):
        self.DATABASE_DICT["default"]["CONN_MAX_AGE"] = None
        return self.DATABASE_DICT

    TIME_ZONE = "America/Edmonton"
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = True
    # If you set this to False, Django will not format dates, numbers and
    # calendars according to the current locale
    USE_L10N = True
    # Use timezone support
    USE_TZ = True

    SITE_ID = 1
    ROOT_URLCONF = "{{cookiecutter.package_name}}.urls"

    # Requires the secret key to be stored in a environment variable called
    # SECRET_KEY.
    SECRET_KEY = values.SecretValue()

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [project_path("templates")],
            "OPTIONS": {
                "debug": False,
                "loaders": [
                    (
                        "django.template.loaders.cached.Loader",
                        [
                            "django.template.loaders.filesystem.Loader",
                            "django.template.loaders.app_directories.Loader",
                        ],
                    ),
                ],
                "context_processors": [
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.request",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.contrib.messages.context_processors.messages",
                ],
                "libraries": {
                    "staticfiles": "django.templatetags.static",
                },
            },
        },
    ]

    MIDDLEWARE_CLASSES = [
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    ]

    INSTALLED_APPS = [
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.admin",
        "django.contrib.flatpages",
        "django.contrib.staticfiles",
        "django_extensions",
        "storages",
        "{{cookiecutter.package_name}}.users",
    ]

    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.postmarkapp.com"
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = values.Value(environ_prefix="", environ_name="POSTMARK_API_TOKEN")
    EMAIL_HOST_PASSWORD = values.Value(
        environ_prefix="", environ_name="POSTMARK_API_TOKEN"
    )

    # Absolute filesystem path to the directory that will hold user-uploaded
    # files.
    # Example: "/home/media/media.lawrence.com/media/"
    MEDIA_ROOT = project_path("public/media")
    # URL that handles the media served from MEDIA_ROOT. Make sure to use a
    # trailing slash.
    # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
    MEDIA_URL = "/media/"

    # Absolute path to the directory static files should be collected to.
    # Don't put anything in this directory yourself; store your static files
    # in apps' "static/" subdirectories and in STATICFILES_DIRS.
    # Example: "/home/media/media.lawrence.com/static/"
    STATIC_ROOT = project_path("public/static/")
    # URL prefix for static files.
    # Example: "http://media.lawrence.com/static/"
    STATIC_URL = "/static/"
    # Additional project_paths of static files
    STATICFILES_DIRS = (project_path("static/"),)
    # List of finder classes that know how to find static files in
    # various project_paths.
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )
    # This is adding MD5 hashes to static files and stores the mapping of
    # staticfiles and MD5 hashes in the cache backend. There's an alternative
    # backend storing in a Manifest file but cache is probably more performant.
    STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"  # noqa
    )

    # URL prefix for admin static files -- CSS, JavaScript and images.
    # Make sure to use a trailing slash.
    # Examples: "http://foo.com/static/admin/", "/static/admin/".
    ADMIN_MEDIA_PREFIX = "/static/admin/"

    # Use cached sessions by default
    SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
    SESSION_COOKIE_HTTPONLY = True

    AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

    RAVEN_CONFIG = {"dsn": values.Value("", environ_name="RAVEN_DSN")}
