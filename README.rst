Introduction
============

``bobtemplates.niteoweb`` provides `mr.bob`_ templates to generate packages for
`NiteoWeb`_ projects.

Available templates are:

    -   ``plone``: a template for a full featured Plone add-on, including:

        -   zc.buildout best practices

        -   GenericSetup install profile

        -   Zope 3 browser layer

        -   z3c.jbot overrides folder

        -   static/ resourceDirectory for serving static resources

        -   Sphinx documentation

        -   test suite with 100% test coverage

        -   Travis CI integration

    -   ``pyramid``: not done yet ...


Global settings
---------------

Some variables are used with every template.  These should be added to the
mr.bob config so you don't have to answer them every time. Example:

    [variables]

    author.name = NiteoWeb Ltd.
    author.email = info@niteoweb.com
    author.github.user = niteoweb


Creating a add-on package
-------------------------

To create a Plone add-on run::

    $ mrbob -O niteoweb.zulu bobtemplates.niteoweb:plone

and answer the questions::

    Welcome to mr.bob interactive mode. Before we generate directory structure,
    some questions need to be answered.

    Answer with a question mark to display help.
    Value in square brackets at the end of the questions present default value
    if there is no answer.


    --> Name of the package: niteoweb.zulu

    --> Version of the package [0.1]:

    --> License of the package [BSD]:

Your package is now ready. Let's build the development environment and see
if all tests pass::

    $ cd niteoweb.zulu
    $ make

Great, you are now ready to start Zope in foreground mode: ``bin/instance fg``.
Once Zope is up, point your browser to ``http://localhost:8080``, login as
``admin:admin``, create a new Plone site while selecting ``niteoweb.zulu`` from
the list of Add-ons and voilá: a Plone site with your very own add-on
installed.

Now you can add some customizations to views and templates, or maybe write some
CSS and JS.

.. _mr.bob: http://mrbob.readthedocs.org/en/latest/
.. _NiteoWeb: http://www.niteoweb.com
