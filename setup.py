import os

from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pjson',
    author='Igor Guerrero',
    author_email='igfgt1@gmail.com',
    description=('Command-line tool to validate and pretty-print JSON and XML.'),
    license='MIT',
    keywords='json xml',
    url='http://igorgue.com/pjson',
    version='0.1',
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': ['pjson = pjson:main']
    },
    install_requires=[
        'Pygments==1.5'
    ]
)
