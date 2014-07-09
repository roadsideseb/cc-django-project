# -*- encoding: utf-8 -*-
import os
import pytest
import django

from configurations import importer

from django_webtest import DjangoTestApp, WebTestMixin

os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


def pytest_configure():
    importer.install()
    django.setup()


@pytest.fixture(scope='function')
def webtest(request, transactional_db):
    """
    Provide the "app" object from WebTest as a fixture
    Taken and adapted from https://gist.github.com/magopian/6673250
    """
    # Patch settings on startup
    wtm = WebTestMixin()
    wtm._patch_settings()

    # Unpatch settings on teardown
    request.addfinalizer(wtm._unpatch_settings)

    return DjangoTestApp()
