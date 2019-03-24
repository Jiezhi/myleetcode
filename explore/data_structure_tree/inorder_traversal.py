#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-24

Leetcode: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

"""
from tree_node import *


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        ret = []
        if not root:
            return ret
        if root.left:
            ret = ret + self.inorderTraversal(root.left)
        ret.append(root.val)
        if root.right:
            ret = ret + self.inorderTraversal(root.right)
        return ret


if __name__ == '__main__':
    assert Solution().inorderTraversal(build_tree_node([1, None, 2, 3])) == [1, 3, 2]
