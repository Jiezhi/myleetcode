#!/usr/bin/env python
"""
CREATED AT: 2022/3/10
Des:

https://leetcode.com/problems/n-ary-tree-preorder-traversal/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        Runtime: 69 ms, faster than 55.77%
        Memory Usage: 16.4 MB, less than 13.05%

        The number of nodes in the tree is in the range [0, 10^4].
        0 <= Node.val <= 10^4
        The height of the n-ary tree is less than or equal to 1000.
        """
        if not root:
            return []
        ret = [root.val]
        for c in root.children:
            ret += self.preorder(c)
        return ret


def test():
    # No test here
    pass


if __name__ == '__main__':
    test()
