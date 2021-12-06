#!/usr/bin/env python
"""
CREATED AT: 2021/12/5
Des:

https://leetcode.com/problems/house-robber-iii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
from functools import lru_cache
from typing import Optional

from src.tree_node import TreeNode, build_tree_node


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 56 ms, faster than 46.90%
        Memory Usage: 18.8 MB, less than 7.40%
        The number of nodes in the tree is in the range [1, 10^4].
        0 <= Node.val <= 10^4
        :param root:
        :return:
        """

        # @lru_cache(None)
        # need lru_cache for large tree, but it also requires TreeNode to be hashable.
        # FixMe made TreeNode hashable.
        def sub_rob(root, parent_robbed):
            if root is None:
                return 0
            if parent_robbed:
                return sub_rob(root.left, False) + sub_rob(root.right, False)
            else:
                return max(
                    root.val + sub_rob(root.left, True) + sub_rob(root.right, True),
                    sub_rob(root.left, False) + sub_rob(root.right, False)
                )

        return max(
            sub_rob(root.left, False) + sub_rob(root.right, False),
            root.val + sub_rob(root.left, True) + sub_rob(root.right, True)
        )


def test():
    null = None
    assert Solution().rob(root=build_tree_node([8, 1, null, 1, null, null, 9])) == 17
    assert Solution().rob(root=build_tree_node([3])) == 3
    assert Solution().rob(root=build_tree_node([3, 1, 4])) == 5
    assert Solution().rob(root=build_tree_node([3, 1, 1])) == 3
    assert Solution().rob(root=build_tree_node([3, 2, 3, null, 3, null, 1])) == 7
    assert Solution().rob(root=build_tree_node([3, 4, 5, 1, 3, null, 1])) == 9


if __name__ == '__main__':
    test()
