#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-04-24

Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""
from tree_node import *


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 1
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth


def test():
    assert Solution().maxDepth(build_tree_node([3, 9, 20, None, None, 15, 7])) == 3


if __name__ == '__main__':
    test()
