#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-18

Leetcode: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

"""
from tree_node import *


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        ret = []
        if not root:
            return ret
        ret.append(root.val)
        if root.left:
            ret = ret + self.preorderTraversal(root.left)
        if root.right:
            ret = ret + self.preorderTraversal(root.right)
        return ret


if __name__ == '__main__':
    assert Solution().preorderTraversal(build_tree_node([1, None, 2, 3])) == [1, 2, 3]
