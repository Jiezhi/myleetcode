#!/usr/bin/env python
"""
CREATED AT: 2021/12/7
Des:

https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from list_node import ListNode, buildListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        Runtime: 24 ms, faster than 96.78% of Python3
        Memory Usage: 14.3 MB, less than 40.23% of Python3
        The Linked List is not empty.
        Number of nodes will not exceed 30.
        Each node's value is either 0 or 1.
        :param head:
        :return:
        """
        if head is None:
            return 0
        ret = head.val
        while head.next is not None:
            head = head.next
            ret = (ret << 1) + head.val
        return ret


def test():
    assert Solution().getDecimalValue(head=buildListNode([1, 0, 1])) == 5
    assert Solution().getDecimalValue(head=buildListNode([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) == 18880
    assert Solution().getDecimalValue(head=buildListNode([0, 0])) == 0


if __name__ == '__main__':
    test()
