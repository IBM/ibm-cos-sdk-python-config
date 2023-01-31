#!/usr/bin/env python
# Copyright 2019, 2020 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import pkg_resources

__version__ = '2.0.0'
PACKAGE_NAME = 'ibm_cos_sdk_config'
PACKAGE_DESC = 'IBM COS Resource Configuration SDK for Python'

with open('requirements.txt') as f:
    install_requires = [
        str(req) for req in pkg_resources.parse_requirements(f)
    ]
with open('requirements-dev.txt') as f:
    tests_require = [str(req) for req in pkg_resources.parse_requirements(f)]

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name=PACKAGE_NAME.replace('_', '-'),
    version=__version__,
    description=PACKAGE_DESC,
    license='Apache 2.0',
    install_requires=install_requires,
    tests_require=tests_require,
    author='IBM',
    author_email='cossdk@us.ibm.com',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/IBM/ibm-cos-sdk-python-config',
    packages=[PACKAGE_NAME],
    include_package_data=True,
    keywords=PACKAGE_NAME,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    zip_safe=True)
