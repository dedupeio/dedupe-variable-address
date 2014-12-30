try:
    from setuptools import setup, Extension
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")


setup(
    name='dedupe-variable-address',
    #url='https://github.com/datamade/dedupe',
    version='0.0.0.2',
    #description='A python library for accurate and scaleable data deduplication and entity-resolution',
    packages=['dedupe.variables'],
    install_requires=['usaddress', 'dedupe'],
    #ext_modules=[Extension('dedupe.cpredicates', ['src/cpredicates.c'])],
    #license='The MIT License: http://www.opensource.org/licenses/mit-license.php
    )
