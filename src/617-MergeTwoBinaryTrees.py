#!/usr/bin/env python
"""
CREATED AT: 2022/3/5
Des:

https://leetcode.com/problems/merge-two-binary-trees/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import Optional

from tree_node import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Runtime: 180 ms, faster than 7.78%
        Memory Usage: 15.4 MB, less than 71.67%

        The number of nodes in both trees is in the range [0, 2000].
        -10^4 <= Node.val <= 10^4
        """
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


def test():
    assert Solution().mergeTrees(TreeNode(1), TreeNode(2)) == TreeNode(3)
    assert Solution().mergeTrees(TreeNode(1), None) == TreeNode(1)


if __name__ == '__main__':
    test()
