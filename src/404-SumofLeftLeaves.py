#!/usr/bin/env python
"""
CREATED AT: 2021/11/4
Des:

https://leetcode.com/problems/sum-of-left-leaves/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: Tree

See: 
"""
import collections
from typing import Optional

from src.tree_node import TreeNode, build_tree_node


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 32 ms, faster than 80.36%
        Memory Usage: 14.6 MB, less than 77.97%
        :param root:
        :return:
        """
        if root is None:
            return 0
        dq = collections.deque()
        ret = 0
        dq.append(root)
        while len(dq) > 0:
            node = dq.pop()
            if node.left is not None and node.left.left is None and node.left.right is None:
                ret += node.left.val
            elif node.left is not None:
                dq.append(node.left)
            if node.right is not None:
                dq.append(node.right)
        return ret


def test():
    null = None
    assert Solution().sumOfLeftLeaves(root=build_tree_node([3, 9, 20, null, null, 15, 7])) == 24
    assert Solution().sumOfLeftLeaves(root=build_tree_node([1])) == 0


if __name__ == '__main__':
    test()
