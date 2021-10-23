#!/usr/bin/env python
"""
Created on 

Des: buld ntree node for https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
from typing import List

null = None


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def build_nary_node(nums):
    # TODO build nary node for test
    pass


if __name__ == '__main__':
    build_nary_node(nums=[1, null, 3, 2, 4, null, 5, 6])
