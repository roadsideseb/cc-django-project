# -*- coding: utf-8 -*-
from __future__ import absolute_import

from configurations import values

from .base import Base


class Prod(Base):
    DEBUG = False
    TEMPLATE_DEBUG = False

    EMAIL_SUBJECT_PREFIX = '[{{cookiecutter.repo_name}}][Prod] '

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'djlibcloud',
        'raven.contrib.django.raven_compat',
    ]

    STATICFILES_STORAGE = 'djlibcloud.storage.LibCloudStorage'
    STATIC_URL = 'https://<LONG HASH>.ssl.cf4.rackcdn.com/'
    CLOUDFILES_USER = values.Value()
    CLOUDFILES_API_KEY = values.Value()

    ALLOWED_HOSTS = ['{{cookiecutter.repo_name}}.apps.roadsi.de']

    RAVEN_DSN = values.Value()

    POSTGRESQL_DB = values.Value(
        environ_name="POSTGRES_ENV_POSTGRESQL_DB", environ_prefix='')
    POSTGRESQL_USER = values.Value(
        environ_name="POSTGRES_ENV_POSTGRESQL_USER", environ_prefix='')
    POSTGRESQL_PASS = values.Value(
        environ_name="POSTGRES_ENV_POSTGRESQL_PASS", environ_prefix='')
    POSTGRES_HOST = values.Value(
        environ_name='POSTGRES_PORT_5432_TCP_ADDR', environ_prefix='')
    POSTGRES_PORT = values.Value(
        environ_name='POSTGRES_PORT_5432_TCP_PORT', environ_prefix='')

    ALLOWED_HOSTS = ['{{cookiecutter.repo_name}}.apps.roadsi.de']

    @property
    def DATABASES(self):
        return {'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': self.POSTGRESQL_DB,
            'USER': self.POSTGRESQL_USER,
            'PASSWORD': self.POSTGRESQL_PASS,
            'HOST': self.POSTGRES_PORT_5432_TCP_ADDR,
            'PORT': self.POSTGRES_PORT_5432_TCP_PORT}}

    @property
    def LIBCLOUD_PROVIDERS(self):
        return {
            'default': {
                'type': 'libcloud.storage.types.Provider.CLOUDFILES',
                'user': self.CLOUDFILES_USER,
                'key': self.CLOUDFILES_API_KEY,
                'bucket': '{{cookiecutter.repo_name}}',
                'region': 'syd'}}

    @property
    def RAVEN_CONFIG(self):
        return {'dsn': self.RAVEN_DSN}
