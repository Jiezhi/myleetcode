#!/usr/bin/env python
"""
CREATED AT: 2021/12/29
Des:

https://leetcode.com/problems/distribute-coins-in-binary-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:

Ref: https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/

Time Spent:  min
"""
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 65 ms, faster than 5.19%
        Memory Usage: 14.2 MB, less than 62.42%
        The number of nodes in the tree is n.
        1 <= n <= 100
        0 <= Node.val <= n
        The sum of all Node.val is n.
        :param root:
        :return:
        """
        ret = 0

        def dfs(node):
            nonlocal ret
            if not node:
                return 0
            left_move = dfs(node.left)
            right_move = dfs(node.right)
            ret += abs(left_move) + abs(right_move)
            return node.val + left_move + right_move - 1

        dfs(root)
        return ret


def test():
    assert Solution().distributeCoins(root=build_tree_node([3, 0, 0])) == 2
    assert Solution().distributeCoins(root=build_tree_node([0, 3, 0])) == 3


if __name__ == '__main__':
    test()
