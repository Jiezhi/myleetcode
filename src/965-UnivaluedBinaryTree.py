#!/usr/bin/env python
"""
CREATED AT: 2022/4/27
Des:
https://leetcode.com/problems/univalued-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""

from typing import Optional
from tree_node import TreeNode


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        """
        Runtime: 50 ms, faster than 30.94%
        Memory Usage: 13.8 MB, less than 61.94%

        The number of nodes in the tree is in the range [1, 100].
        0 <= Node.val < 100
        """

        def isValid(node) -> bool:
            if not node:
                return True
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False
            return isValid(node.left) and isValid(node.right)

        return isValid(root)


def test():
    assert Solution().isUnivalTree(TreeNode.from_list([1, 1, 1, 1, 1, None, None, None]))


if __name__ == '__main__':
    test()
