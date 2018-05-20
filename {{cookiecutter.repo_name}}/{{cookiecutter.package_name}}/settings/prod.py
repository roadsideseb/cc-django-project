from configurations import values

from .base import Base, project_path


class Production(Base):
    DEBUG = False

    STATIC_ROOT = project_path('../staticfiles')

    EMAIL_SUBJECT_PREFIX = '[{{cookiecutter.repo_name}}][Prod] '

    INSTALLED_APPS = Base.INSTALLED_APPS + [
        'raven.contrib.django.raven_compat',
    ]

    DATABASES = values.DatabaseURLValue()
    ALLOWED_HOSTS = ['{{cookiecutter.subdomain}}.herokuapp.com']

    MEDIA_URL = 'https://s3.amazonaws.com/{{cookiecutter.subdomain}}/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = values.Value(environ_prefix='')
    AWS_SECRET_ACCESS_KEY = values.Value(environ_prefix='')
    AWS_STORAGE_BUCKET_NAME = values.Value(environ_prefix='')

    @property
    def LIBCLOUD_PROVIDERS(self):
        if not self.AWS_ACCESS_KEY_ID and not self.AWS_SECRET_ACCESS_KEY:
            raise ValueError('AWS credentials not provided')
        return {
            'default': {
                'type': 'libcloud.storage.types.Provider.S3',
                'user': self.AWS_ACCESS_KEY_ID,
                'key': self.AWS_SECRET_ACCESS_KEY,
                'bucket': self.AWS_STORAGE_BUCKET_NAME,
                'secure': True}}

    RAVEN_DSN = values.Value()

    @property
    def RAVEN_CONFIG(self):
        return {'dsn': self.RAVEN_DSN}
