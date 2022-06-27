#!/usr/bin/env python
"""
CREATED AT: 2021/12/14
Des:

https://leetcode.com/problems/range-sum-of-bst/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: BST

See: 

Time Spent: 10 min
"""
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Runtime: 200 ms, faster than 88.66% of Python3
        Memory Usage: 22.3 MB, less than 59.19% of Python3

        :param root: The number of nodes in the tree is in the range [1, 2 * 10^4].
            1 <= Node.val <= 10^5
            All Node.val are unique.
        :param low:  1 <= low <= high <= 10^5
        :param high:  1 <= low <= high <= 10^5
        :return:
        """
        if not root:
            return 0
        if high < root.val:
            return self.rangeSumBST(root.left, low, high)
        if low > root.val:
            return self.rangeSumBST(root.right, low, high)
        ret = 0
        if root and low <= root.val <= high:
            ret += root.val
            ret += self.rangeSumBST(root.left, low, high)
            ret += self.rangeSumBST(root.right, low, high)
        return ret


def test():
    null = None
    assert Solution().rangeSumBST(root=build_tree_node([10, 5, 15, 3, 7, null, 18]), low=7, high=15) == 32
    assert Solution().rangeSumBST(root=build_tree_node([10, 5, 15, 3, 7, 13, 18, 1, null, 6]), low=6, high=10) == 23


if __name__ == '__main__':
    test()
