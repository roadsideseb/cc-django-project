{{ cookiecutter.project_title }}
===============================


.. image:: https://travis-ci.com/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}.svg
    :target: https://travis-ci.com/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}


Set Up Development Environment
------------------------------

Create a virtual environment and clone this repository::

    $ mkvirtualenv {{cookiecutter.repo_name}}
    $ git clone git@github.com:{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}.git
    $ cd {{cookiecutter.repo_name}}
    $ setvirtualenvproject

The next thing to do is to install all the requirements for the project. Since
we are setting up the development environment and will require additional
packages for that, we'll use the ``dev.txt`` requirement file::

    $ pip install -r requirements-dev.txt


Setup Docker & Docker Compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are using **Docker Compose** to run our development environment. If you
haven't worked with it before, you should take a look at `the documentation on
Docker Compose <https://docs.docker.com/compose/overview/>`__.

The first thing we have to do is to install Docker and the tool
``docker-compose``. If you are on **a Mac**, you want to install theu
`Docker Toolbox <https://docs.docker.com/mac/step_one/>`__ or the the new
`Docker for Mac <https://beta.docker.com/>`__.

Or **on Linux** check out the `install section
<https://docs.docker.com/compose/install/>`__ in the docs on how to set it up.


Running the Dev Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

With Docker Engine and Compose installed, we can build and run the development
environment::

    $ docker-compose build

The full set up of all containers is started by executing::

    $ docker-compose up

which will build containers (if required), start all of them and attach to 
their output. The containers can be shut down with ``Ctrl + C``.


Django Configuration
~~~~~~~~~~~~~~~~~~~~

This project uses `django-configurations`_ to handle Django settings. It is a
thin wrapper around the ``settings.py`` that modularises the values and makes
it easier to extend and override different settings "profiles". This project
uses the following profiles:


+-----------+-------------------------------------------+-----------------------+
| **Dev**   | Local development setup.                  | ``settings/dev.py``   |
+-----------+-------------------------------------------+-----------------------+
| **CI**    | Used for CI-specific settings.            | ``settings/ci.py``    |
+-----------+-------------------------------------------+-----------------------+
| **Prod**  | Settings for the test/stage/prod servers. | ``settings/prod.py``  |
+-----------+-------------------------------------------+-----------------------+

The configuration profiles are preconfigured in ``conftest.py``, ``manage.py``
and the respective *WSGI* files for the servers. To override the default simply
specify the ``DJANGO_CONFIGURATION`` setting in the shell or provide the
``--configuration`` option to ``manage.py``. These two commands are essentially
the same::

    $ ./manage.py runserver --configuration=CI
    $ DJANGO_CONFIGURATION=CI ./manage.py runserver

Another advantage of *django-configurations* is that it provides an easy way to
overwrite settings when running a command by manipulating environmental
variables. Things such as API keys, the Django secret key and other values
should not be stored in version control but be passed at runtime. To make this
process as simple as possible, we recommend to create a ``environment.sh``
file in the ``www`` directory and export variables there::

    $ echo "export DJANGO_SECRET_KEY='my special secret key'" > environment.sh

You can now source the ``environment.sh`` file once when you activate the
virtual environment and all variables available::

    $ source environment.sh

The file is in the ``.gitignore`` and won't (and shouldn't) be added to the
repository. You could also add the sourcing of the file to you ``postactivate``
script for virtualenvwrapper.


.. _`django-configurations`: http://django-configurations.readthedocs.org/en/latest/


Running Django
~~~~~~~~~~~~~~

Create the initial database and apply all migrations::

    $ ./manage.py migrate

This should set up your database(s) assuming that you have docker environment
running. After that, start the server and check out the website in your browser
at http://localhost:8000::

    $ ./manage.py runserver


.. _`docs on new migrations`: https://docs.djangoproject.com/en/dev/topics/migrations/


Running Tests
-------------

For a full test run including *PEP8* checking run *py.test* with the PEP8
plugin::

    $ py.test --pep8

Running the full test suite with PEP8 checking and coverage report, run::

    $ py.test --pep8 --cov {{ cookiecutter.package_name }} --cov-report html

which will create a ``htmlcov`` directory containing nicely formatted coverage
reports that you can look at in the browser.


Running CI Test
~~~~~~~~~~~~~~~

The full test suite including PEP8 and coverage will be run on `Travis`_ every
time a commit is pushed to github or a pull request is created.
