#!/usr/bin/env python
"""
CREATED AT: 2021/10/26
Des:

https://leetcode.com/problems/invert-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: Tree

See: 
"""
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Runtime: 28 ms, faster than 91.21%
        Memory Usage: 14.2 MB, less than 46.18%
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100
        :param root:
        :return:
        """
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def test():
    assert Solution().invertTree(root=build_tree_node([])) == build_tree_node([])
    assert Solution().invertTree(root=build_tree_node([1])) == build_tree_node([1])
    assert Solution().invertTree(root=build_tree_node([1, 2])) == build_tree_node([1, None, 2])
    assert Solution().invertTree(root=build_tree_node([1, 2, 3])) == build_tree_node([1, 3, 2])
    assert Solution().invertTree(root=build_tree_node([4, 2, 7, 1, 3, 6, 9])) == build_tree_node([4, 7, 2, 9, 6, 3, 1])


if __name__ == '__main__':
    test()
