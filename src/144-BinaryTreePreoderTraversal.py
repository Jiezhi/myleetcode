#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-03-24

Leetcode: https://leetcode.com/problems/binary-tree-preorder-traversal/

same as https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

"""
from tree_node import *


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        ans = []
        tmp = root
        stack = []
        while tmp or len(stack) > 0:
            if tmp:
                ans.append(tmp.val)
                stack.append(tmp)
                tmp = tmp.left
            else:
                tmp = stack.pop()
                tmp = tmp.right
        return ans


def test():
    assert Solution().preorderTraversal(build_tree_node([1, None, 2, 3])) == [1, 2, 3]
