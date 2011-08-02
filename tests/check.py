#!/usr/bin/python
import sys
import testmodule


def windows():
    assert testmodule.X().windows_only() == 5
    assert not hasattr(testmodule.X, 'unix_only')
    assert not hasattr(testmodule.X(), 'unix_only')


def not_windows():
    assert testmodule.X().unix_only() == 6
    assert not hasattr(testmodule.X, 'windows_only')
    assert not hasattr(testmodule.X(), 'windows_only')


def debug():
    assert getattr(testmodule, 'debug') == 25


def not_debug():
    assert not hasattr(testmodule, 'debug')


config = int(sys.argv[1])
if config == 0:
    not_debug()
    not_windows()
elif config == 1:
    not_debug()
    windows()
elif config == 2:
    debug()
    not_windows()
elif config == 3:
    debug()
    windows()
else:
    sys.exit('Invalid argument')
print 'checked', config
