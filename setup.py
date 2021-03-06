#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Kirill V. Lyadvinsky
# http://www.codeatcpp.com
#
# Copyright (c) InfoTeCS JSC. All rights reserved.
# Licensed under the MIT license. See LICENSE file
# in the project root for full license information.
#
""" Setup script """

from setuptools import setup, find_packages
from domain_tools.__init__ import __version__ as VERSION_INFO

with open('README.rst') as readme_file:
    LONG_README = readme_file.read()

DEV_REQUIRES = [
    'coverage>=3.7.1',
    'setuptools>=32.1.3',
    'pep8>=1.7.0'
]

INSTALL_REQ = [
    'ldap3>=2.1.1',
]

setup(
    name='domain_tools',
    version=VERSION_INFO,
    description='Parse and import domain structure',
    keywords='ldap domain tools utility import users windows ldaps',
    long_description=LONG_README,
    author='Kirill V. Lyadvinsky',
    author_email='mail@codeatcpp.com',
    download_url='https://github.com/Infotecs/domain_tools',
    url='https://github.com/Infotecs/domain_tools',
    license='MIT License',
    packages=find_packages(exclude=('test', 'docs')),
    extras_require={
        'test': DEV_REQUIRES,
    },
    install_requires=INSTALL_REQ,
    test_suite='test',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'get_ldap_users = domain_tools.get_ldap_users:main',
        ],
    },
)
