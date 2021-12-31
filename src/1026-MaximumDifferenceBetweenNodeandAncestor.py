#!/usr/bin/env python
"""
CREATED AT: 2021/12/31
Des:

https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: Tree, DFS

See: 

Time Spent: 10 min
"""
from typing import Optional

from src.tree_node import TreeNode, build_tree_node


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 65 ms, faster than 13.99%
        Memory Usage: 21.2 MB, less than 9.00%
        The number of nodes in the tree is in the range [2, 5000].
        0 <= Node.val <= 10^5
        :param root:
        :return:
        """

        def dfs(node) -> (int, int, int):
            """
            :param node:
            :return: max diff, min num, max num
            """
            if not node:
                return None, None, None
            left_diff, left_min, left_max = dfs(node.left)
            right_diff, right_min, right_max = dfs(node.right)
            if not left_diff and not right_diff:
                # leaf
                return -1, node.val, node.val
            elif not left_diff:
                # only has right children
                return max(abs(node.val - right_max), abs(node.val - right_min), right_diff), \
                       min(node.val, right_min), max(node.val, right_max)
            elif not right_diff:
                # only has left children
                return max(abs(node.val - left_max), abs(node.val - left_min), left_diff), \
                       min(node.val, left_min), max(node.val, left_max)
            else:
                # has both left and right children
                return max(
                    abs(node.val - right_max), abs(node.val - right_min), right_diff,
                    abs(node.val - left_max), abs(node.val - left_min), left_diff
                ), min(node.val, left_min, right_min), max(node.val, left_max, right_max)

        ret, _, _ = dfs(root)
        return ret


def test():
    null = None
    assert Solution().maxAncestorDiff(root=build_tree_node([8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13])) == 7
    assert Solution().maxAncestorDiff(root=build_tree_node([1, null, 2, null, 0, 3])) == 3


if __name__ == '__main__':
    test()
