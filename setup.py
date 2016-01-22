#!/usr/bin/env python
"""
Setup file for pyhaystack
"""
import pyhaystack.info as info

from distutils.core import setup

import re
import os
import requests

os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'


setup(name='pyhaystack',
      version=info.__version__,
	 description='Python Haystack Utility',
      author=info.__author__,
      author_email=info.__author_email__,
      url='http://www.project-haystack.com/',
      keywords = ['tags', 'hvac', 'project-haystack', 'building', 'automation', 'analytic'],
	 long_description = "\n".join(info.__doc__.split('\n')),
	 install_requires = [
          'requests',
          'setuptools',
          'pandas',
          'parsimonious', 
          'iso8601', 
          'hszinc'],
      packages=[
          'pyhaystack',
          'pyhaystack.client', 
          'pyhaystack.haystackIO',
          'pyhaystack.history',
          'pyhaystack.util',
          'pyhaystack.server',],
#      entry_points={
#          'console_scripts': ['pyhaystack=pyhaystack:main'],
#     },
      long_description=open('README.rst').read(),
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: System :: Networking",
          "Topic :: Utilities",
          ],)