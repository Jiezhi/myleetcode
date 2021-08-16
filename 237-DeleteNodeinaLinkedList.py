#!/usr/bin/env python
"""
CREATED AT: 2021/8/16
Des:
https://leetcode.com/problems/delete-node-in-a-linked-list/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/553/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from list_node import ListNode, buildListNode


class Solution:
    def deleteNode(self, node: ListNode):
        """
        41 / 41 test cases passed.
        Status: Accepted
        Runtime: 40 ms
        Memory Usage: 14.9 MB
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


def test():
    # No test case applied.
    pass


if __name__ == '__main__':
    test()
