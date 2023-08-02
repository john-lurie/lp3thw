try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Gothons from Planet Percal #25',
    'author': 'John C. Lurie',
    'version': '0.1',
    'install_requires': ['flask'],
    'packages': ['gothonweb'],
    'scripts': [''],
    'name': 'gothonweb'
}

setup(**config)
