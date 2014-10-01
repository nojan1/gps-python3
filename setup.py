
"""Simple port of the standard Python2 "gps" package to Python3. 
All of the functionality remains unchanged from the original and only changes required for operation in Python3 have been made.
All credit goes to the original authors as shown in the copyright below. Information on copying and distribution of source code can be found in the COPYING file copied from their original source code.
Compilation copyright is held by the GPSD project. All rights reserved.
GPSD project copyrights are assigned to the project lead, currently Eric S. Raymond. Other portions of the GPSD code are Copyright (c) 1997, 1998, 1999, 2000, 2001, 2002 by Remco Treffkorn, and others Copyright (c) 2005 by Eric S. Raymond. For other copyrights, see individual files.
"""

import sys
from setuptools import setup
from distutils.core import Extension

doclines = __doc__.splitlines()

setup(
    name='gps',
    version=1.0,
    author="Niklas Hedlund",
    author_email="nojan1989@gmail.com",
	url="https://github.com/nojan1/gps-python3",
    packages=["gps"]
    )
