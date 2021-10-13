#!/usr/bin/env python
"""
CREATED AT: 2021/10/13
Des:

https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""

from typing import List, Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        Runtime: 48 ms, faster than 26.03%
        Memory Usage: 14.2 MB, less than 90.87%
        1 <= preorder.length <= 100
        1 <= preorder[i] <= 108
        All the values of preorder are unique.
        :param preorder:
        :return:
        """
        n = len(preorder)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        i = 1
        while i < n and preorder[i] < preorder[0]:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root


def test():
    null = None
    assert Solution().bstFromPreorder(preorder=[4, 2]) == build_tree_node([4, 2])
    assert Solution().bstFromPreorder(preorder=[8, 5, 1, 7, 10, 12]) == build_tree_node([8, 5, 10, 1, 7, null, 12])
    assert Solution().bstFromPreorder(preorder=[1, 3]) == build_tree_node([1, null, 3])


if __name__ == '__main__':
    test()
