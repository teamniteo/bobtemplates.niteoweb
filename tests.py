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
        #root_dir = os.path.join(os.path.dirname(__file__), '../', '../',)
        options = {
            'dir': os.path.join(os.path.dirname(__file__)),
            'template': self.template,
        }
        return self.env.run(
            '%(dir)s/bin/mrbob -O collective.foo --config '
            '%(dir)s/test_answers.ini %(dir)s/bobtemplates/%(template)s'
            % options)


class PloneTemplateTest(BaseTemplateTest):
    template = 'plone'

    def test_everything(self):
        result = self.create_template()
        self.assertItemsEqual(
            result.files_created.keys(),
            [
                'collective.foo',
                'collective.foo/.travis.yml',
                'collective.foo/MANIFEST.in',
                'collective.foo/Makefile',
                'collective.foo/README.rst',
                'collective.foo/bootstrap.py',
                'collective.foo/buildout.cfg',
                'collective.foo/buildout.d',
                'collective.foo/buildout.d/base.cfg',
                'collective.foo/buildout.d/development.cfg',
                'collective.foo/buildout.d/travis.cfg',
                'collective.foo/buildout.d/versions.cfg',
                'collective.foo/docs',
                'collective.foo/docs/CHANGELOG.rst',
                'collective.foo/docs/LICENSE.rst',
                'collective.foo/docs/api.rst',
                'collective.foo/docs/conf.py',
                'collective.foo/docs/glossary.rst',
                'collective.foo/docs/index.rst',
                'collective.foo/setup.py',
                'collective.foo/src',
                'collective.foo/src/collective',
                'collective.foo/src/collective/__init__.py',
                'collective.foo/src/collective/foo',
                'collective.foo/src/collective/foo/__init__.py',
                'collective.foo/src/collective/foo/browser',
                'collective.foo/src/collective/foo/browser/__init__.py',
                'collective.foo/src/collective/foo/browser/configure.zcml',
                'collective.foo/src/collective/foo/browser/overrides',
                'collective.foo/src/collective/foo/browser/overrides/.gitignore',
                'collective.foo/src/collective/foo/browser/static',
                'collective.foo/src/collective/foo/browser/static/.gitignore',
                'collective.foo/src/collective/foo/configure.zcml',
                'collective.foo/src/collective/foo/interfaces.py',
                'collective.foo/src/collective/foo/profiles',
                'collective.foo/src/collective/foo/profiles/default',
                'collective.foo/src/collective/foo/profiles/default/browserlayer.xml',
                'collective.foo/src/collective/foo/profiles/default/metadata.xml',
                'collective.foo/src/collective/foo/testing.py',
                'collective.foo/src/collective/foo/tests',
                'collective.foo/src/collective/foo/tests/__init__.py',
                'collective.foo/src/collective/foo/tests/test_setup.py',
            ]
        )
