#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-04-24

Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Reference: https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2374/

Tail Recursion

"""
from tree_node import *


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 1
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth

    def maxDepth2(self, root: TreeNode):
        """
        Tail Recursion Version
        :param root:
        :return:
        """

        def helper(tree, acc):
            if not tree:
                return acc
            return max(helper(tree.left, acc + 1), helper(tree.right, acc + 1))

        return helper(root, 0)


def test():
    assert Solution().maxDepth(build_tree_node([3, 9, 20, None, None, 15, 7])) == 3
    assert Solution().maxDepth(build_tree_node([2, None, 3, None, 4, None, 5, None, 6])) == 5
    assert Solution().maxDepth2(build_tree_node([3, 9, 20, None, None, 15, 7])) == 3
    assert Solution().maxDepth2(build_tree_node([2, None, 3, None, 4, None, 5, None, 6])) == 5


if __name__ == '__main__':
    test()
