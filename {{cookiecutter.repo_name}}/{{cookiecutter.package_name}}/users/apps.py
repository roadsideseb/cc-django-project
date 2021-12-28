from __future__ import unicode_literals, absolute_import
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersAppConfig(AppConfig):
    name = "{{cookiecutter.package_name}}.users"
    verbose_name = _("Users")
