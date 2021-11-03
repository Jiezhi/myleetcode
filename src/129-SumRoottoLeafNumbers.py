#!/usr/bin/env python
"""
CREATED AT: 2021/11/3
Des:

https://leetcode.com/problems/sum-root-to-leaf-numbers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: Tree

See: 
"""
from typing import Optional

from src.tree_node import TreeNode, build_tree_node


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 32 ms, faster than 72.26%
        Memory Usage: 14.2 MB, less than 79.39%
        The number of nodes in the tree is in the range [1, 1000].
        0 <= Node.val <= 9
        The depth of the tree will not exceed 10.
        :param root:
        :return:
        """

        def dfs(tree: TreeNode, parentVal: int):
            if tree is None:
                return 0
            curVal = parentVal * 10 + tree.val
            if tree.left is None and tree.right is None:
                return curVal
            return dfs(tree.left, curVal) + dfs(tree.right, curVal)

        return dfs(root, 0)


def test():
    assert Solution().sumNumbers(root=build_tree_node([3])) == 3
    assert Solution().sumNumbers(root=build_tree_node([1, 2, 3])) == 25
    assert Solution().sumNumbers(root=build_tree_node([4, 9, 0, 5, 1])) == 1026


if __name__ == '__main__':
    test()
