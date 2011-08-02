import os
from distutils.core import Extension, setup

TESTCONFIG = int(os.environ['TESTCONFIG'])

configs = [[],
           [('_WIN32', '1')],
           [('DEBUG', '1')],
           [('_WIN32', '1'), ('DEBUG', '1')]]

macros = configs[TESTCONFIG]
print 'using config', macros

setup(ext_modules=[Extension(name='testmodule', sources=['testmodule.c'], define_macros=macros)])
