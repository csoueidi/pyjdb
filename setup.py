# from setuptools import setup, find_packages
#
# setup(
#     name='pyjdwp',
#     version='0.1',
#     author="Christopher Suter",
#     author_email="cgs@alltheburritos.com",
#     url="https://github.com/csuter/pyjdb",
#     project_urls={
#         "Source Code": "https://github.com/csuter/pyjdb",
#     },
#     packages=find_packages(),
#     package_data={
#         'pyjdwp': ['specs/jdwp.spec*'],
#     },
#     install_requires=[
#         'pyparsing',
#     ],
#     python_requires='>=3.9',
# )
from setuptools import setup, find_packages
import os

# Utility function to read the README file.
# Used for the long_description. It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyjdwp',
    version='0.1',
    author="Christopher Suter",
    author_email="cgs@alltheburritos.com",
    description=("A Python library for debugging Java programs using the Java Debug Wire Protocol (JDWP)."),
    long_description=read('README.md'),  # Set the content of README.md as the long description
    long_description_content_type='text/markdown',  # This is important to ensure that markdown is rendered correctly on PyPI
    url="https://github.com/csuter/pyjdb",
    project_urls={
        "Source Code": "https://github.com/csuter/pyjdb",
    },
    packages=find_packages(),
    package_data={
        'pyjdwp': ['specs/jdwp.spec*'],
    },
    install_requires=[
        'pyparsing',
    ],
    python_requires='>=3.9',
)
