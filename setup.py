#!usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
    name = 'my_app',
    version = '1.0',
    license = 'GNU General Public Licence v3',
    author = 'xmark2',
    author_email = 'xmark2@gmail.com',
    description = 'Hello world app for Flask',
    packages = ['my_app'],
    platform = 'any',
    install_requires = [
        'flask',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)