#! /usr/bin/env python

# Copyright (c) 2007, PediaPress GmbH
# See README.txt for additional licensing information.

import os
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup
import distutils.util

version=None
execfile(distutils.util.convert_path('mwlib/rl/_version.py')) 
# adds 'version' to local namespace

install_requires=["mwlib>=0.8.3.dev, <0.9.0", "pygments>=0.10", "mwlib.ext>=0.8.2"]

def read_long_description():
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.txt")
    return open(fn).read()

setup(
    name="mwlib.rl",
    version=str(version),
    entry_points = {
        'mwlib.writers': ['rl = mwlib.rl.rlwriter:writer'],
    },
    install_requires=install_requires,
    packages=["mwlib", "mwlib.rl", "mwlib.fonts"],
    namespace_packages=['mwlib'],
    zip_safe=False,
    include_package_data=True,
    url = "http://code.pediapress.com/",
    description="generate pdfs from mediawiki markup",
    long_description = read_long_description(),
    license="BSD License",
    maintainer="pediapress.com",
    maintainer_email="info@pediapress.com",
)
