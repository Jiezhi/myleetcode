#!/usr/bin/env python
"""
CREATED AT: 2021/8/29
Des:

https://leetcode.com/problems/intersection-of-two-linked-lists/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import collections
from typing import Optional

from list_node import ListNode, buildListNode


class Solution:
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        AC: 06/06/2022
        Runtime: 213 ms, faster than 48.04%
        Memory Usage: 29.5 MB, less than 69.35%
        :param headA:
        :param headB:
        The number of nodes of listA is in the m.
        The number of nodes of listB is in the n.
        1 <= m, n <= 3 * 10^4
        1 <= Node.val <= 10^5
        0 <= skipA < m
        0 <= skipB < n
        intersectVal is 0 if listA and listB do not intersect.
        intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
        :return:
        """
        tailA = headA
        while tailA.next:
            tailA = tailA.next

        tailA.next = headB
        # if two list has intersection, then there would be cycle in the headA list now.
        fast, slow = headA.next.next, headA.next
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        if not fast or not fast.next:
            tailA.next = None
            return None

        fast = headA
        while fast != slow:
            fast = fast.next
            slow = slow.next
        tailA.next = None
        return slow

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
