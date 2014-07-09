Django Project Template
=======================

This is the boiler plate for a Django project using `cookiecutter`_ as the 
project generator. This template is loosely based on `pydanny's Django
template`_


Create a new project
--------------------

A project is set up in an isolated virtual environment so we need to set that
up first, before we can use the cookiecutter template to create a new project.
The following examples assume that you have ``virtualenvwrapper`` installed::

  $ mkvirtualenv sample-project  # activates venv automatically
  $ pip install cookiecutter
  $ cookiecutter ....


.. _`cookiecutter`: http://cookiecutter.rtfd.org/
.. _`pydanny's Django template`: https://github.com/pydanny/cookiecutter-django
