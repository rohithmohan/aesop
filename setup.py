# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='aesop',
    version='1.1.0',
    description='Module for analyzing electrostatics with protein structures',
    long_description=readme,
    author='Reed Harrison, Rohith Mohan',
    author_email='reed.harrison@email.ucr.edu, rohith.mohan@email.ucr.edu',
    url='https://github.com/rohithmohan/aesop-python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'data')),
#    install_requires=['prody', 'gridDataFormats', 'scipy', 'numpy', 'python-dateutil'], # Commented out for ReadTheDocs
    include_package_data=True,
#    package_data={
#        'aesop-python':
#            ['README.rst',
#            'LICENSE',
#            ],
#    },
    zip_safe=False	
)

