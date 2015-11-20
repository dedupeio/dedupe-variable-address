try:
    from setuptools import setup, Extension
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")


setup(
    name='dedupe-variable-address',
    url='https://github.com/datamade/dedupe-variables-address',
    version='0.0.5',
    description='Address variable type for dedupe',
    packages=['dedupe.variables'],
    install_requires=['usaddress', 'parseratorvariable >= 0.0.10', 'future'],
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php'
    )
