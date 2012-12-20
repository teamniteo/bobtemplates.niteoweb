Introduction
============

``bobtemplates.niteoweb`` provides `mr.bob`_ templates to generate packages for
Plone and Pyramid projects. Templates are designed to be reusable by others,
individuals and teams. All templates have tests for verifying which files and
folders were generated, along with tests that run on the actual generated
package.

Available templates are:

* `Plone`_: a template for a full featured Plone add-on, including:

  * zc.buildout best practices
  * GenericSetup install profile
  * Zope 3 browser layer
  * `z3c.jbot`_ overrides folder
  * ``static/`` resourceDirectory for serving static resources (images, CSS,
    JS, etc.)
  * `Sphinx`_ documentation
  * test suite with a solid test coverage
  * `Travis CI`_ integration

* `Pyramid`_: a template for a full featured Pyramid project, work-in-progress.


Global settings
---------------

Some answers to bob's questions can be pre-filled based on global configuration
so you don't have to answer them every time. You can store this configuration
either on you local computer, or if you are working in a team, somewhere
online. We, at `NiteoWeb Ltd.`_, for example, have these answers always
available for us at http://www.niteoweb.com/mrbob.ini.


Creating a Plone add-on package
-------------------------------

To create a Plone add-on first install (or upgrade to latest) the
``bobtemplates.niteoweb`` package and then run `mrbob`::

    $ easy_install -U bobtemplates.niteoweb
    $ mrbob --config ~/.mrbob.ini -O collective.foo bobtemplates:plone

Then answer some questions::

    Welcome to mr.bob interactive mode. Before we generate directory structure,
    some questions need to be answered.

    Answer with a question mark to display help.
    Value in square brackets at the end of the questions present default value
    if there is no answer.


    --> Name of the package: foo
    (namespace is already set in the ~/.mrbob.ini)

    ...

And your package is ready! Let's build the development environment and see
if all tests pass::

    $ cd collective.foo
    $ make

Great, you are now set to start Zope in foreground mode: ``bin/instance fg``.
Once Zope is up, point your browser to ``http://localhost:8080``, login as
``admin:admin``, create a new Plone site while selecting ``collective.foo``
from the list of Add-ons and voilá: a Plone site with your very own add-on
installed.

Now you can add some customizations to views and templates, or maybe write some
CSS and JS.

.. _mr.bob: http://mrbob.readthedocs.org/en/latest/
.. _NiteoWeb Ltd.: http://www.niteoweb.com
.. _Plone: http://plone.org
.. _Pyramid: http://docs.pylonsproject.org/en/latest/
.. _z3c.jbot: http://pypi.python.org/pypi/z3c.jbot
.. _Sphinx: http://sphinx-doc.org/
.. _Travis CI: http://travis-ci.org/
