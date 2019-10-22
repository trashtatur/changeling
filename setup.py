from setuptools import setup, find_packages

setup(
    name='portal',
    version='0.2',
    packages = find_packages(),
    author= 'Andreas Hoerster',
    install_requires=[
        'PyYAML',
        'Click',
        'schema'
    ],
    entry_points='''
        [console_scripts]
        portal=portal.CLI.cli:cli
    ''',
)