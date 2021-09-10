#!/usr/bin/env python
"""
CREATED AT: 2021/9/10
Des:

https://leetcode.com/problems/balanced-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
import collections
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        228 / 228 test cases passed.
        Status: Accepted
        Runtime: 52 ms
        Memory Usage: 19.4 MB
        :param root:
        :return:
        """

        def compare_child(node: TreeNode):
            if not node:
                return True, 0
            lb, ldep = compare_child(node.left)
            rb, rdep = compare_child(node.right)
            return lb and rb and abs(ldep - rdep) < 2, max(ldep, rdep) + 1

        balanced, rdep = compare_child(root)
        return balanced


def test():
    null = None
    assert Solution().isBalanced(root=build_tree_node([]))
    assert not Solution().isBalanced(root=build_tree_node([1, 2, 2, 3, 3, null, null, 4, 4]))
    assert Solution().isBalanced(root=build_tree_node([3, 9, 20, null, null, 15, 7]))


if __name__ == '__main__':
    test()
