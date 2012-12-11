from setuptools import find_packages
from setuptools import setup

version = '0.2a1'

setup(
    name='bobtemplates.kotti',
    version=version,
    description="mr.bob templates for Kotti development",
    long_description=open("README.rst").read() + "\n" +
                     open("CHANGES.rst").read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/bobtemplates.kotti',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    entry_points={},
)
