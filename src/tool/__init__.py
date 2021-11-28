#!/usr/bin/env python
"""
Created on 20210809

Des:

"""
import collections


def print_results(fn):
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        print(ret)
        return ret

    return wrapper


def equal_list_value(list_a, list_b) -> bool:
    return collections.Counter(list_a) == collections.Counter(list_b)


def test():
    assert equal_list_value(None, None)
    assert equal_list_value([], [])
    assert equal_list_value([1, 2], [2, 1])
    assert not equal_list_value([1], [])


if __name__ == '__main__':
    test()
