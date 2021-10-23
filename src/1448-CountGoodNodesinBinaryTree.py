#!/usr/bin/env python
"""
CREATED AT: 2021/8/17
Des:
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3899/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

from tree_node import *


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        63 / 63 test cases passed.
        Status: Accepted
        Runtime: 244 ms
        Memory Usage: 31.5 MB
        :param root:
        :return:
        """
        good_nodes = 1
        dq = collections.deque()
        dq.append(root)
        while len(dq) > 0:
            node = dq.pop()
            if node.left:
                if node.val <= node.left.val:
                    good_nodes += 1
                else:
                    node.left.val = node.val
                dq.append(node.left)
            if node.right:
                if node.val <= node.right.val:
                    good_nodes += 1
                else:
                    node.right.val = node.val
                dq.append(node.right)

        return good_nodes


def test():
    null = None
    assert Solution().goodNodes(build_tree_node([3, 1, 4, 3, null, 1, 5])) == 4
    assert Solution().goodNodes(build_tree_node([3, 3, null, 4, 2])) == 3
    assert Solution().goodNodes(build_tree_node([1])) == 1


if __name__ == '__main__':
    test()
