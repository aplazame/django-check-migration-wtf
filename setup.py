import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(
    name='django-check-migration-wtf',
    version='1.4.0',
    packages=find_packages(),
    description='A line of description',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Antonio Irizar',
    author_email='antonioirizar@gmail.com',
    url='https://github.com/antonioIrizar/django-check-migration-wtf',
    license='GLP3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
    ],
    keywords='django postgres postgresql migrations',
    python_requires='>=3.7',
    install_requires=[
        'Django>=2.2,<6.0',
        'PyGithub>=1.50,<2',
    ]
)
