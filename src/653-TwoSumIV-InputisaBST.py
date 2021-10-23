#!/usr/bin/env python
"""
CREATED AT: 2021/8/23
Des:

https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3908/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Optional

import tree_node
from tree_node import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        422 / 422 test cases passed.
        Status: Accepted
        Runtime: 92 ms
        Memory Usage: 16.4 MB
        :param root:
        :param k:
        :return:
        """

        def find_num(num) -> bool:
            node = root
            while node:
                if num == node.val:
                    return True
                if num < node.val:
                    node = node.left
                else:
                    node = node.right
            return False

        dq = collections.deque()
        dq.append(root)
        while len(dq) > 0:
            node = dq.pop()
            # filter node.val itself
            if node.val * 2 != k and find_num(k - node.val):
                return True
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return False


def test():
    null = None
    assert Solution().findTarget(tree_node.build_tree_node([5, 3, 6, 2, 4, null, 7]), k=9)
    assert not Solution().findTarget(tree_node.build_tree_node([5, 3, 6, 2, 4, null, 7]), k=28)
    assert Solution().findTarget(tree_node.build_tree_node([2, 1, 3]), k=4)
    assert not Solution().findTarget(tree_node.build_tree_node([1]), k=2)


if __name__ == '__main__':
    test()
