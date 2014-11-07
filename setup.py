#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='djangochurch-data',
    version='0.1',
    description='Initial data for Django Church projects',
    long_description=open('README.rst').read(),
    url='https://github.com/djangochurch/djangochurch-data',
    maintainer='Alex Tomkins',
    maintainer_email='alex@blanc.ltd.uk',
    platforms=['any'],
    packages=find_packages(),
    package_data={'djangochurch_data': [
        'fixtures/*.json',
        'images/*.jpg',
    ]},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    license='BSD',
)
