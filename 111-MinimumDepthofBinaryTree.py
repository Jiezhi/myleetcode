#!/usr/bin/env python
"""
CREATED AT: 2021/9/18
Des:
https://leetcode.com/problems/minimum-depth-of-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        52 / 52 test cases passed.
        Status: Accepted
        Runtime: 840 ms
        Memory Usage: 48.9 MB
        :param root:
        :return:
        """
        if root is None:
            return 0
        current_level = [root]
        ret = 0
        while len(current_level) > 0:
            ret += 1
            next_level = []
            for n in current_level:
                if n.left is None and n.right is None:
                    return ret
                if n.left is not None:
                    next_level.append(n.left)
                if n.right is not None:
                    next_level.append(n.right)
            current_level = next_level


def test():
    null = None
    assert Solution().minDepth(root=build_tree_node([3, 9, 20, null, null, 15, 7])) == 2
    assert Solution().minDepth(root=build_tree_node([2, null, 3, null, 4, null, 5, null, 6])) == 5


if __name__ == '__main__':
    test()
