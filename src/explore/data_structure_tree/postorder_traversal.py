#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-24

Leetcode: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/

See also: 145

"""
from tree_node import *


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        ret = []
        if not root:
            return ret
        if root.left:
            ret = ret + self.postorderTraversal(root.left)
        if root.right:
            ret = ret + self.postorderTraversal(root.right)
        ret.append(root.val)
        return ret


if __name__ == '__main__':
    assert Solution().postorderTraversal(build_tree_node([1, None, 2, 3])) == [3, 2, 1]
