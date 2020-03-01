from setuptools import setup, find_packages

setup(
    name='skeleton',
    version='0.1',
    description='',
    author='',
    author_email='behren2@protonmail.com',
    keywords='skeleton',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.5',
    install_requires=['remodel', 'schema'],
    include_package_data=True,
)