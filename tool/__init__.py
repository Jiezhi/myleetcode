#!/usr/bin/env python
"""
Created on 20210809

Des:

"""
from typing import List

from tree_node import TreeNode, get_tree_node_list


def print_results(fn):
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        print(ret)
        return ret

    return wrapper
