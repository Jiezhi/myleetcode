#!/usr/bin/env python
"""
Created on 2022/7/20

Author: 

Des:

"""
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


class Clock:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result

        return clocked
