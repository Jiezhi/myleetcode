#!/usr/bin/env python
"""
CREATED AT: 2021/8/29
Des:

https://leetcode.com/problems/intersection-of-two-linked-lists/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import collections

from list_node import ListNode, buildListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        39 / 39 test cases passed.
        Status: Accepted
        Runtime: 152 ms
        Memory Usage: 29.2 MB
        :param headA:
        :param headB:
        :return:
        """
        dqA = collections.deque()
        dqB = collections.deque()
        node = headA
        while node is not None:
            dqA.append(node)
            node = node.next
        node = headB
        while node is not None:
            dqB.append(node)
            node = node.next
        if len(dqA) == 0 or len(dqB) == 0:
            return None
        while len(dqA) > 0 and len(dqB) > 0:
            node = dqA.pop()
            if node != dqB.pop():
                return node.next
        return node


def test():
    headA = buildListNode([4, 1, 8, 4, 5])
    headB = buildListNode([5, 6, 1, 8, 4, 5])
    assert Solution().getIntersectionNode(headA=headA, headB=headB) == buildListNode([1, 8, 4, 5])

    headA = buildListNode([2, 4, 6])
    headB = buildListNode([1, 5])
    assert Solution().getIntersectionNode(headA=headA, headB=headB) is None

    headA = buildListNode([3])
    headB = buildListNode([2, 3])
    assert Solution().getIntersectionNode(headA=headA, headB=headB) == buildListNode([3])


if __name__ == '__main__':
    test()
