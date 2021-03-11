#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([a-z0-9._-]+)['"]''')


def get_version():
    '''
    Get the SDK version number
    :return:
    '''
    init = open(os.path.join(ROOT, 'cos_config', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='ibm-cos-sdk-config',
    version=get_version(),
    description='IBM Config SDK for Python',
    long_description=open('README.md').read(),
    author='IBM',
    author_email='',
    url='https://github.com/IBM/ibm-cos-sdk-python-config',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    python_requires='~=3.6',
    install_requires=[
        'ibm-cloud-sdk-core>=0.5.3,<1.0.0',
    ],
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
