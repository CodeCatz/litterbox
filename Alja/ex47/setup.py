try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Exercise 47 from Learn Python the Hard Way',
	'author': 'iAlja',
	'url': 'URL to get it at.',
	'download_url': 'where to download it.',
	'author_email': 'ialja@me.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)