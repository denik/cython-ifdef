#!/usr/bin/python
import sys
import os

def system(cmd):
    if os.system(cmd):
        sys.exit(1)

system('../cython_ifdef.py testmodule.pyx')


for index in range(4):
    system('./clean')
    system('TESTCONFIG=%s python setup.py build_ext --inplace' % index)
    system('python check.py %s' % index)

print 'all good'
