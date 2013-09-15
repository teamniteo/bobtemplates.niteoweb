import unittest2 as unittest
import os
import tempfile
import shutil

from scripttest import TestFileEnvironment


class BaseTemplateTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

        # docs http://pythonpaste.org/scripttest/
        self.env = TestFileEnvironment(
            os.path.join(self.tempdir, 'test-output'),
            ignore_hidden=False,
        )

    def create_template(self):
        """Run mr.bob to create your template."""
        options = {
            'dir': os.path.join(os.path.dirname(__file__)),
            'template': self.template,
            'project': self.project,
        }
        return self.env.run(
            '%(dir)s/bin/mrbob -O %(project)s --config '
            '%(dir)s/test_answers.ini %(dir)s/bobtemplates/%(template)s'
            % options)


class PloneTemplateTest(BaseTemplateTest):
    """Tests for the `plone` template."""
    template = 'plone'
    project = 'collective.foo'

    def test_plone_template(self):
        """Test the `plone` template.

        Generate a project from a template and test which files were created.
        """
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                self.project,
                self.project + '/.gitignore',
                self.project + '/.travis.yml',
                self.project + '/MANIFEST.in',
                self.project + '/Makefile',
                self.project + '/README.rst',
                self.project + '/bootstrap.py',
                self.project + '/buildout.cfg',
                self.project + '/buildout.d',
                self.project + '/buildout.d/base.cfg',
                self.project + '/buildout.d/development.cfg',
                self.project + '/buildout.d/travis.cfg',
                self.project + '/buildout.d/versions.cfg',
                self.project + '/docs',
                self.project + '/docs/CHANGELOG.rst',
                self.project + '/docs/LICENSE.rst',
                self.project + '/docs/api.rst',
                self.project + '/docs/conf.py',
                self.project + '/docs/glossary.rst',
                self.project + '/docs/index.rst',
                self.project + '/docs/_static',
                self.project + '/docs/_static/.gitkeep',
                self.project + '/setup.py',
                self.project + '/src',
                self.project + '/src/collective',
                self.project + '/src/collective/__init__.py',
                self.project + '/src/collective/foo',
                self.project + '/src/collective/foo/__init__.py',
                self.project + '/src/collective/foo/browser',
                self.project + '/src/collective/foo/browser/__init__.py',
                self.project + '/src/collective/foo/browser/configure.zcml',
                self.project + '/src/collective/foo/browser/overrides',
                self.project + '/src/collective/foo/browser/overrides/.gitkeep',
                self.project + '/src/collective/foo/browser/static',
                self.project + '/src/collective/foo/browser/static/.gitkeep',
                self.project + '/src/collective/foo/configure.zcml',
                self.project + '/src/collective/foo/interfaces.py',
                self.project + '/src/collective/foo/profiles',
                self.project + '/src/collective/foo/profiles/default',
                self.project + '/src/collective/foo/profiles/default/browserlayer.xml',
                self.project + '/src/collective/foo/profiles/default/metadata.xml',
                self.project + '/src/collective/foo/testing.py',
                self.project + '/src/collective/foo/tests',
                self.project + '/src/collective/foo/tests/__init__.py',
                self.project + '/src/collective/foo/tests/test_setup.py',
            ]
        )


class PyramidTemplateTest(BaseTemplateTest):
    """Tests for the `pyramid` template."""
    template = 'pyramid'
    project = 'foo'

    def test_pyramid_template(self):
        """Test the `pyramid` template.

        Generate a project from a template and test which files were created.
        """
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                self.project,
                self.project + '/.coveralls.yml',
                self.project + '/.gitignore',
                self.project + '/.travis.yml',
                self.project + '/MANIFEST.in',
                self.project + '/Makefile',
                self.project + '/Procfile',
                self.project + '/README.rst',
                self.project + '/bootstrap.py',
                self.project + '/buildout.cfg',
                self.project + '/buildout.d',
                self.project + '/buildout.d/base.cfg',
                self.project + '/buildout.d/development.cfg',
                self.project + '/buildout.d/travis.cfg',
                self.project + '/buildout.d/versions.cfg',
                self.project + '/docs',
                self.project + '/docs/CHANGELOG.rst',
                self.project + '/docs/LICENSE.rst',
                self.project + '/docs/_static',
                self.project + '/docs/_static/.gitkeep',
                self.project + '/docs/conf.py',
                self.project + '/docs/deploy.rst',
                self.project + '/docs/develop.rst',
                self.project + '/docs/glossary.rst',
                self.project + '/docs/index.rst',
                self.project + '/etc',
                self.project + '/etc/development.ini',
                self.project + '/etc/production.ini',
                self.project + '/requirements.txt',
                self.project + '/runtime.txt',
                self.project + '/setup.cfg',
                self.project + '/setup.py',
                self.project + '/src',
                self.project + '/src/foo',
                self.project + '/src/foo/__init__.py',
                self.project + '/src/foo/models.py',
                self.project + '/src/foo/scripts',
                self.project + '/src/foo/scripts/__init__.py',
                self.project + '/src/foo/scripts/populate.py',
                self.project + '/src/foo/static',
                self.project + '/src/foo/static/bootstrap-alert.js',
                self.project + '/src/foo/static/bootstrap-button.js',
                self.project + '/src/foo/static/bootstrap-carousel.js',
                self.project + '/src/foo/static/bootstrap-collapse.js',
                self.project + '/src/foo/static/bootstrap-dropdown.js',
                self.project + '/src/foo/static/bootstrap-modal.js',
                self.project + '/src/foo/static/bootstrap-popover.js',
                self.project + '/src/foo/static/bootstrap-responsive.css',
                self.project + '/src/foo/static/bootstrap-scrollspy.js',
                self.project + '/src/foo/static/bootstrap-tab.js',
                self.project + '/src/foo/static/bootstrap-tooltip.js',
                self.project + '/src/foo/static/bootstrap-transition.js',
                self.project + '/src/foo/static/bootstrap-typeahead.js',
                self.project + '/src/foo/static/bootstrap.css',
                self.project + '/src/foo/static/favicon.ico',
                self.project + '/src/foo/static/foo.css',
                self.project + '/src/foo/static/foo.js',
                self.project + '/src/foo/static/glyphicons-halflings-white.png',
                self.project + '/src/foo/static/glyphicons-halflings.png',
                self.project + '/src/foo/static/html5shiv.js',
                self.project + '/src/foo/static/jquery.js',
                self.project + '/src/foo/static/logo.png',
                self.project + '/src/foo/templates',
                self.project + '/src/foo/templates/404.pt',
                self.project + '/src/foo/templates/home.pt',
                self.project + '/src/foo/templates/main_template.pt',
                self.project + '/src/foo/tests.py',
                self.project + '/src/foo/views.py',
            ]
        )
