from setuptools import setup, find_packages
from pjson import __version__

setup(
    name='pjson',
    author='Igor Guerrero',
    author_email='igfgt1@gmail.com',
    description=('Command-line tool to validate and pretty-print JSON and XML.'),
    license='MIT',
    keywords='json xml',
    url='http://igorgue.com/pjson',
    version=__version__,
    packages=find_packages(),
    package_data = {
        # If any package contains *.txt or *.md files, include them:
        '': ['*.md', 'LICENSE'],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': ['pjson = pjson:main']
    },
    install_requires=[
        'Pygments>=1.6',
        'xmlformatter==0.1.1',
    ]
)
