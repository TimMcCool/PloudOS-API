from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'PloudOS API interactions like starting servers etc.'
LONG_DESCRIPTION = 'A PloudOS API wrapper that allows connecting to PloudOS accounts and interacting with the PloudOS API.'

# Setting up
setup(
    name="PloudosAPI",
    version=VERSION,
    author="TimMcCool",c
    author_email="timmccool.scratch@gmail.com",
    description=DESCRIPTION,
    #long_description_content_type="text/markdown",
    #long_description=long_description,
    packages=find_packages(),
    install_requires=['http', 'requests', 'json'],
    keywords=['python', 'ploudos', 'api', 'ploudos api', 'ploudos api wrapper'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
© 2022 GitHub, Inc.
Terms
Privacy
