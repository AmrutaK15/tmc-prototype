#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the SKATestDevice project
#
#
#

import os
import sys
from setuptools import setup

setup_dir = os.path.dirname(os.path.abspath(__file__))

# make sure we use latest info from local code
sys.path.insert(0, setup_dir)

readme_filename = os.path.join(setup_dir, 'README.rst')
with open(readme_filename) as file:
    long_description = file.read()

release_filename = os.path.join(setup_dir, 'SKATestDevice', 'release.py')
exec(open(release_filename).read())

pack = ['SKATestDevice']

setup(name=name,
      version=version,
      description='A generic Test device for testing SKA base class functionalites.',
      packages=pack,
      include_package_data=True,
      test_suite="test",
      entry_points={'console_scripts':['SKATestDevice = SKATestDevice:main']},
      author='cam',
      author_email='cam at ska.ac.za',
      license='BSD-3-Clause',
      long_description=long_description,
      url='www.tango-controls.org',
      platforms="All Platforms"
      )