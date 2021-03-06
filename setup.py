#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup

from require import __version__

version_str = '.'.join(str(n) for n in __version__)

# In order for coverage to work, we don't install any packages when
# tox is running the tests
packages = []
package_data = {}
if os.environ.get('TOX_ENV') is None:
    packages = [
        'require',
        'require.management',
        'require.management.commands',
        'require.templatetags',
    ]
    package_data = {
        'require': [
            'resources/*.jar',
            'resources/*.js',
            'resources/tests/*.js',
        ],
    }

setup(
    name='django-require2',
    version=version_str,
    license='BSD',
    description=(
        'A Django staticfiles post-processor for optimizing with RequireJS.'),
    author='László Károlyi',
    author_email='laszlo@karolyi.hu',
    url='https://github.com/karolyi/django-require2',
    test_suite='tests',
    packages=packages,
    package_data=package_data,
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
