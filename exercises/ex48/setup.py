try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LP3THW Exercise 48',
    'author': 'John C. Lurie',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['lexicon'],
    'scripts': [''],
    'name': 'ex48'
}

setup(**config)
