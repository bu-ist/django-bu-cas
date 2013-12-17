from distutils.core import setup

setup(
	name='django-bu-cas',
	version='1.2.0',
	author='Fyodor Wolf',
	author_email='fwolf@bu.edu',
	packages=['django_bucas',],
	url='http://github.com/bu-ist/django-bu-cas',
	license='LICENSE.txt',
	description='CAS Authentication middleware for the BU Django environment',
	long_description=open('README.md').read(),
	install_requires=[
		"Django >= 1.5",
	],
)
