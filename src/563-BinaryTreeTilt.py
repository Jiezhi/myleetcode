#!/usr/bin/env python
"""
CREATED AT: 2021/12/8
Des:

https://leetcode.com/problems/binary-tree-tilt/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import Optional

from src.tree_node import TreeNode, build_tree_node


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 50 ms, faster than 91.86% of Python3
        Memory Usage: 16.2 MB, less than 65.52% of Python3

        The number of nodes in the tree is in the range [0, 10^4].
        -1000 <= Node.val <= 1000
        :param root:
        :return:
        """
        ret = 0

        def dfs(root: TreeNode) -> int:
            """
            :param root:
            :return: sum
            """
            nonlocal ret
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            l = dfs(root.left)
            r = dfs(root.right)
            ret += abs(l - r)
            return l + r + root.val

        dfs(root)
        return ret


def test():
    assert Solution().findTilt(root=build_tree_node([])) == 0
    assert Solution().findTilt(root=build_tree_node([1, 2, 3])) == 1
    assert Solution().findTilt(root=build_tree_node([4, 2, 9, 3, 5, None, 7])) == 15
    assert Solution().findTilt(root=build_tree_node([21, 7, 14, 1, 1, 2, 2, 3, 3])) == 9


if __name__ == '__main__':
    test()
