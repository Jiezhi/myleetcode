#!/usr/bin/env python
"""
https://leetcode.com/problems/same-tree/description/
Created on 2018-11-18

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val:
                return False
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        # this can be omit if (not p and q) or (p and not q):
        return False


def test():
    # to build build TreeNode is  tricky, so just let leetcode to test code
    pass
