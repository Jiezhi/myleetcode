#!/usr/bin/env python
"""
CREATED AT: 2022/3/21
Des:
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""

from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Runtime: 57 ms, faster than 45.13%
        Memory Usage: 15.3 MB, less than 11.69%

        Do not return anything, modify root in-place instead.
        The number of nodes in the tree is in the range [0, 2000].
        -100 <= Node.val <= 100
        """

        def dfs(node: Optional[TreeNode]) -> (Optional[TreeNode], Optional[TreeNode]):
            """
            return head and tail node
            """
            if not node:
                return None, None
            if not node.left and not node.right:
                return node, node
            left_head, left_tail = dfs(node.left)
            right_head, right_tail = dfs(node.right)
            if left_tail:
                left_tail.right = right_head
                node.right = left_head
            if not right_tail:
                right_tail = left_tail
            node.left = None

            return node, right_tail

        dfs(root)


def test():
    tree = build_tree_node([1, 2, None, 3])
    Solution().flatten(tree)
    assert tree == build_tree_node([1, None, 2, None, 3])


if __name__ == '__main__':
    test()
