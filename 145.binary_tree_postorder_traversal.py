#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-25

Leetcode: https://leetcode.com/problems/binary-tree-postorder-traversal/

Same as: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/

"""
from tree_node import *


class Solution:
    # Recursive solution could be found at explore/data_structure_tree/postorder_traversal.py
    def postorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        ret = []
        stack = []
        tmp = root
        while tmp or len(stack) > 0:
            if tmp:
                stack.append(tmp)
                ret.append(tmp.val)
                # ret.insert(0, tmp.val)
                tmp = tmp.right
            else:
                tmp = stack.pop()
                tmp = tmp.left
        ret.reverse()
        return ret


if __name__ == '__main__':
    assert Solution().postorderTraversal(build_tree_node([1, None, 2, 3])) == [3, 2, 1]
