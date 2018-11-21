from distutils.core import setup, Extension
setup(name = 'linalg', version = '1.0',  \
   ext_modules = [Extension('linalg', ['linalg.c'])])