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
        p = root
        q = []
        while p or len(q) > 0:
            while p:
                ans.append(p.val)
                q.append(p)
                p = p.left
            if len(q) > 0:
                p = q.pop()
                p = p.right
        return ans


if __name__ == '__main__':
    assert Solution().preorderTraversal(build_tree_node([1, None, 2, 3])) == [1, 2, 3]
