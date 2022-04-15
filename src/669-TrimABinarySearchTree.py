#!/usr/bin/env python
"""
CREATED AT: 2022/4/15
Des:
https://leetcode.com/problems/trim-a-binary-search-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import Optional
from tree_node import TreeNode


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        Runtime: 56 ms, faster than 79.50%
        Memory Usage: 18 MB, less than 83.03%

        The number of nodes in the tree in the range [1, 10^4].
        0 <= Node.val <= 10^4
        The value of each node in the tree is unique.
        root is guaranteed to be a valid binary search tree.
        0 <= low <= high <= 10^4
        :param root:
        :param low:
        :param high:
        :return:
        """

        def trim(node: TreeNode):
            if not node:
                return None
            if node.val < low:
                return trim(node.right)
            if node.val > high:
                return trim(node.left)

            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

        return trim(root)


def test():
    assert Solution().trimBST(TreeNode.from_list([1, 0, 2]), 1, 2) == TreeNode.from_list([1, None, 2])
    assert Solution().trimBST(TreeNode.from_list([3, 0, 4, None, 2, None, None, 1]), 1, 3) == TreeNode.from_list(
        [3, 2, None, 1])


if __name__ == '__main__':
    test()
