#!/usr/bin/env python
"""
CREATED AT: 2021/10/11
Des:
https://leetcode.com/problems/diameter-of-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""

from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def getHeight(self, tree):
        if tree is None:
            return 0
        return max(self.getHeight(tree.left), self.getHeight(tree.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 1265 ms, faster than 5.01% of Python3 online submissions
        Memory Usage: 16.2 MB, less than 78.87% of Python3 online submissions
        The number of nodes in the tree is in the range [1, 10**4].
        -100 <= Node.val <= 100
        :param root:
        :return:
        """
        if root is None:
            return 0
        ret = self.getHeight(root.left) + self.getHeight(root.right)
        ret_l = self.diameterOfBinaryTree(root.left)
        ret_r = self.diameterOfBinaryTree(root.right)
        return max(ret, ret_l, ret_r)


def test():
    assert Solution().diameterOfBinaryTree(root=build_tree_node([1, 2, 3, 4, 5])) == 3
    assert Solution().diameterOfBinaryTree(root=build_tree_node([1, 2])) == 1
    l = [x for x in range(10000)]
    assert Solution().diameterOfBinaryTree(root=build_tree_node(l)) == 25
    null = None
    l = [4, -7, -3, null, null, -9, -3, 9, -7, -4, null, 6, null, -6, -6, null, null, 0, 6, 5, null, 9, null, null, -1,
         -4, null, null, null, -2]
    assert Solution().diameterOfBinaryTree(root=build_tree_node(l)) == 8


if __name__ == '__main__':
    test()
