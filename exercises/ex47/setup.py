try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'LP3THW Exercise 47',
    'author': 'John C. Lurie',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'name': 'ex47'
}

setup(**config)

