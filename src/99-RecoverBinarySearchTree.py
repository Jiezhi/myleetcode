#!/usr/bin/env python
"""
CREATED AT: 2022/4/19
Des:

https://leetcode.com/problems/recover-binary-search-tree/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""

from typing import Optional
from tree_node import TreeNode


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Runtime: 88 ms, faster than 63.95%
        Memory Usage: 14.2 MB, less than 65.76%

        Do not return anything, modify root in-place instead.
        The number of nodes in the tree is in the range [2, 1000].
        -2^31 <= Node.val <= 2^31 - 1
        """
        cur, pre, wrong1, wong2 = root, None, None, None
        while cur:
            if not cur.left:
                if pre and pre.val > cur.val:
                    wrong2 = cur
                    if not wrong1:
                        wrong1 = pre
                pre = cur
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if tmp.right == cur:
                    tmp.right = None

                    if pre and pre.val > cur.val:
                        wrong2 = cur
                        if not wrong1:
                            wrong1 = pre
                    pre = cur
                    cur = cur.right
                else:
                    tmp.right = cur
                    cur = cur.left

        wrong1.val, wrong2.val = wrong2.val, wrong1.val


def test():
    # FIX my TreeNode code
    # code contains tmp.right == cur,
    # and would cause infinite loop when there is cycle in tree
    # so just ignore testcase here
    pass
    # null = None
    # tree = TreeNode.from_list([1, 3, null, null, 2])
    # print(Solution().recoverTree(tree))
    # assert tree == TreeNode.from_list(
    #     [3, 1, null, null, 2])


if __name__ == '__main__':
    test()
