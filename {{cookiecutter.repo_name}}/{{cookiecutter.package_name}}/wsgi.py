# -*- coding: utf-8 -*-
import os
import sys

from configurations.wsgi import get_wsgi_application

sys.stdout = sys.stderr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.package_name}}.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

application = get_wsgi_application()
