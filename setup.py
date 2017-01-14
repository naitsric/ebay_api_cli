from setuptools import find_packages, setup


setup(
    name='categories',
    description='A cli program in Python.',
    author='Cristian Duque',
    author_email='anticris9303@gmail.com',
    license='UNLICENSE',
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'docopt',
        'Jinja2',
        'peewee',
        'requests',
        'xmltodict',
    ],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'categories=categories.cli:main',
        ],
    },
)