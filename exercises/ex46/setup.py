try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Monte Carlo simulation to approximate pi',
    'author': 'John C. Lurie',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mcpi'],
    'scripts': ['bin/approxpi'],
    'name': 'mcpi'
}

setup(**config)
