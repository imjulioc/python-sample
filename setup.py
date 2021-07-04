#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import TextIOWrapper
from os import path, system
from sys import executable, exit
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'package-name'
DESCRIPTION = 'Package description.'
LICENSE = 'MIT',
VERSION = '0.0.1'
PYTHON_REQUIRES = '>=3.6.0'
AUTHOR = ''
AUTHOR_EMAIL = ''
URL = 'https://github.com/user/project'

ABOUT = {
    '__version__': VERSION
}

# Packages required for this module to be executed.
INSTALL_REQUIRES = [
    # 'requests'
]

# Optional packages.
EXTRAS_REQUIRE = {
    # 'fancy feature': ['rx'],
}

HERE = path.abspath(path.dirname(__file__))

# Note: this will only work if 'README.md' is present in 'MANIFEST.in'.
readme = (
    open(path.join(HERE, 'README.md'), 'r', encoding='utf-8')
    if path.exists(path.join(HERE, 'README.md'))
    else None
)
readme_isfile = isinstance(readme, TextIOWrapper)

LONG_DESCRIPTION = (
    readme.read()
    if readme_isfile
    else DESCRIPTION
)

readme_isfile and readme.close()


class UploadCommand(Command):
    description = ''
    user_options = []

    @staticmethod
    def status(text):
        # Prints text in bold.
        print(f'\033[1m{text}\033[0m')

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status('Removing previous builds')

        try:
            rmtree(path.join(HERE, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution')

        system(f'{executable} setup.py sdist bdist_wheel --universal')

        exit()


setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license=LICENSE,
    version=ABOUT['__version__'],
    python_requires=PYTHON_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(
        # py_modules=['package'] instead `packages` if the package is a single module.
        exclude=[
            "tests",
            "*.tests",
            "*.tests.*",
            "tests.*"
        ]
    ),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    classifiers=[
        # Trove classifiers
        f'License :: OSI Approved :: {LICENSE} License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'upload': UploadCommand,
    }
)
