from setuptools import setup, find_packages

setup(
    name='changeling',
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
        changeling=changeling.CLI.cli:cli
    ''',
)