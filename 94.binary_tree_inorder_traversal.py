#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-25

Leetcode: https://leetcode.com/problems/binary-tree-inorder-traversal/

Same as: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

"""
from tree_node import *


class Solution:
    # Recursive solution could be found at explore/data_structure_tree/inorder_traversal.py
    def inorderTraversal(self, root: TreeNode) -> list:
        ret = []
        if not root:
            return ret
        stack = []
        tmp = root
        while tmp or len(stack) > 0:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            ret.append(tmp.val)
            tmp = tmp.right

        return ret


if __name__ == '__main__':
    assert Solution().inorderTraversal(build_tree_node([1, None, 2, 3])) == [1, 3, 2]
