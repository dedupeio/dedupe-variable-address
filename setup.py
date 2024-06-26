try:
    from setuptools import setup
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")


setup(
    name='dedupe-variable-address',
    url='https://github.com/datamade/dedupe-variables-address',
    version='1.0.0',
    description='Address variable type for dedupe',
    packages=['addressvariable'],
    install_requires=['usaddress',
                      'parseratorvariable >= 1.0.0'],
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php'
    )
