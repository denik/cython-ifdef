This is [Cython](http://cython.org/) and [Unifdef](http://dotat.at/prog/unifdef/) wrapper that adds some (very basic) preprocessor support to Cython.

`cython_ifdef.py` makes it possible to use preprocessor directives right in your .pyx source:

```python
class X:

#ifdef _WIN32
    def windows_only(self):
        return 5
#else
    def unix_only(self):
        return 6
#endif
```

Running `cython_ifdef.py test.pyx` will produce a `test.c` file that includes appropriate `#ifdef _WIN32` to produce a class that has `windows_only` method when `_WIN32` is defined and `unix_only` when it's not.

Here's an example of what `cython_ifdef.py` can process: [gevent/core_.pyx](https://bitbucket.org/denis/gevent/src/a41fdd222ac2/gevent/core_.pyx#cl-221).

## Installation

In addition to Cython, you need to have Python and [unifdef](http://dotat.at/prog/unifdef/) installed in order to run this script. On Debian/Ubuntu, do `apt-get install unifdef`.

[Download the script from github](https://raw.github.com/denik/cython-ifdef/master/cython_ifdef.py) and put it somewhere on the run path.

## How does it work

* It gets lists of all preprocessor symbols used in the source file using `unifdef -t -s`
* It runs `unifdef` for all possible configurations on the original source.
* For generated source, it runs `cython` and stores the result in memory.
* It then merges all the resulting .c files into one with appropriate #ifdef back in place.

## Limitations

* It only supports symbols that are either defined or undefined. Processing expressions such as `#if SYMBOL == 5` is not implemented.
* It does not look into included .pxi.
* The amount of time it takes is exponential: 2^(Number of symbols), so it does not support arbitrary amount of preprocessor symbols.

It was written to support [gevent's](http://gevent.org) use case, rather than a generic tool, so be warned.

## Author

`cython_ifdef.py` is written by [Denis Bilenko](http://denisbilenko.com) for [gevent project](http://gevent.org) and is licensed under MIT license.