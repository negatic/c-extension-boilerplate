from setuptools import setup, Extensions

setup(
    name='boiler-plate-name',
    version='1',
    ext_modules=[Extensions('_hello', ['_hello.c'])],
)