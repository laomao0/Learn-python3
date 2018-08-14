try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Wangshen',
	'url': 'No url',
	'download_url': 'Where to download it.',
	'author_email': 'My email',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Test1'],
	'scripts': [],
	'name': 'Projecttest'
}

setup(**config)