#!/usr/bin/env python
"""
CREATED AT: 2022/4/16
Des:

https://leetcode.com/problems/convert-bst-to-greater-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 1038

"""
from typing import Optional
from tree_node import TreeNode


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Runtime: 91 ms, faster than 77.72%
        Memory Usage: 16.7 MB, less than 77.23%

        The number of nodes in the tree is in the range [0, 10^4].
        -10^4 <= Node.val <= 10^4
        All the values in the tree are unique.
        root is guaranteed to be a valid binary search tree.
        :param root:
        :return:
        """

        def dfs(node, parent_val) -> int:
            if not node:
                return parent_val
            if not node.left and not node.right:
                node.val += parent_val
                return node.val
            node.val += dfs(node.right, parent_val)
            return dfs(node.left, node.val)

        dfs(root, 0)
        return root


def test():
    null = None
    assert Solution().convertBST(
        TreeNode.from_list([4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8])) == TreeNode.from_list(
        [30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8])


if __name__ == '__main__':
    test()
