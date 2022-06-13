#!/usr/bin/env python

import os
import sys

from setuptools import find_packages, setup

# ADD needed libraries needed for the end user of the package:
# example:
#      requirements = ["numpy", "scipy>=1.0.0", "requests==2.0.1"

requirements = []


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read().replace(".. :changelog", "")


doclink = """
Documentation
-------------

The full documentation can be generated with Sphinx"""


PACKAGE_PATH = os.path.abspath(os.path.join(__file__, os.pardir))

setup(
    name="{{ cookiecutter.repo_name }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_short_description }}",
    entry_points={
        'console_scripts': [
            'cookiecutter.repo_name=cookiecutter.repo_name.cli:main',
        ],
    },    
    long_description=readme + "\n\n" + doclink + "\n\n" + history,
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="https://cosmo-docs.phys.ethz.ch/{{ cookiecutter.repo_name }}",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=requirements,
    license="MIT License",
    zip_safe=False,
    keywords="{{ cookiecutter.repo_name }}",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
)
