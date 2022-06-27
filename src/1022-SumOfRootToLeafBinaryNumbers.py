#!/usr/bin/env python
"""
CREATED AT: 2022/1/11
Des:

https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag:

See:

Time Spent:  min
"""
from typing import Optional

from tree_node import TreeNode, build_tree_node


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 52 ms, faster than 24.89%
        Memory Usage: 14.7 MB, less than 39.83%

        The number of nodes in the tree is in the range [1, 1000].
        Node.val is 0 or 1.
        :param root:
        :return:
        """
        ret = 0

        def dfs(node, num):
            if not node:
                return
            nonlocal ret
            num = (num << 1) | node.val
            if not node.left and not node.right:
                ret += num
                return
            if node.left:
                dfs(node.left, num)
            if node.right:
                dfs(node.right, num)

        dfs(root, 0)
        return ret


def test():
    assert Solution().sumRootToLeaf(root=build_tree_node([1, 1, 1, 1, 1, 1, 1])) == 28
    assert Solution().sumRootToLeaf(root=build_tree_node([1, 0, 1, 0, 1, 0, 1])) == 22
    assert Solution().sumRootToLeaf(root=build_tree_node([0])) == 0


if __name__ == '__main__':
    test()
