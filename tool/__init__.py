#!/usr/bin/env python
"""
Created on 20210809

Des:

"""


def print_results(fn):
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        print(ret)
        return ret

    return wrapper
