import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))

class PyTest(TestCommand):
  user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

  def initialize_options(self):
    TestCommand.initialize_options(self)
    try:
      from multiprocessing import cpu_count
      self.pytest_args = ['-n', str(cpu_count()), '--boxed']
    except (ImportError, NotImplementedError):
      self.pytest_args = ['-n', '1', '--boxed']

  def finalize_options(self):
    TestCommand.finalize_options(self)
    self.test_args = []
    self.test_suite = True

  def run_tests(self):
    import pytest
    errno = pytest.main(self.pytest_args)
    sys.exit(errno)

with open('README.md') as f:
  long_description = f.read()

py_version = sys.version_info[:2]
if py_version < (3, 4):
  raise Exception("aiotf requires Python >= 3.4.")

about = {}
with open(os.path.join(here, 'aiotf', '__version__.py'), 'r') as f:
  exec(f.read(), about)

setup(
  name=about['__title__'],
  version=about['__version__'],
  description=about['__description__'],
  long_description=long_description,
  long_description_content_type='text/markdown',
  author=about['__author__'],
  author_email=about['__author_email__'],
  url=about['__url__'],
  license=about['__license__'],
  packages=find_packages(exclude=('tests', 'docs')),
  python_requires='>=3.4',
  install_requires=[
    'aiogrpc',
    'tensorflow'
  ],
  cmdclass={'test': PyTest},
  classifiers=(
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ),
)
