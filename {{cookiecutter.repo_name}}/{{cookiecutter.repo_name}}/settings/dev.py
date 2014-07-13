# -*- coding: utf-8 -*-
from configurations import values

from . base import Base


class Dev(Base):
    DEBUG = True
    TEMPLATE_DEBUG = True

    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'debug_toolbar.apps.DebugToolbarConfig',
    ]
    MIDDLEWARE_CLASSES = [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ] + Base.MIDDLEWARE_CLASSES
    INTERNAL_IPS = ['127.0.0.1', '::1']

    # We just want to see emails displayed in the console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # This is mainly required for Mac OSX where docker is running in
    # a virtual box. boot2docker will create a host-only interface that
    # forwards all the ports from docker to the host machine.
    # This setting should be used as the host for databases, cache, etc.
    DOCKER_HOST = values.Value('localhost')

    REDIS_HOST = DOCKER_HOST
    REDIS_PORT = 9979

    ALLOWED_HOSTS = ['*']

    @property
    def DATABASES(self):
        return {'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dev_db',
            'USER': 'dev_app',
            'PASSWORD': 'devpassword',
            'HOST': self.DOCKER_HOST,
            'PORT': 9932}}
