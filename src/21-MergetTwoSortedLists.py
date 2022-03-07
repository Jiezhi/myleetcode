#!/usr/bin/env python
"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
Created on 2018-11-11

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
from typing import Optional

from list_node import *


class Solution:
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solved at 2022/03/07
        Runtime: 68 ms, faster than 20.64%
        Memory Usage: 13.9 MB, less than 60.85%

        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.
        """
        if not list2:
            return list1
        if not list1:
            return list2

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = l3 = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return ret.next


def test():
    assert Solution().mergeTwoLists(buildListNode([1, 2, 3]), buildListNode([2, 3, 4])) \
           == buildListNode([1, 2, 2, 3, 3, 4])

    assert Solution().mergeTwoLists2(buildListNode([1, 2, 3]), buildListNode([2, 3, 4])) \
           == buildListNode([1, 2, 2, 3, 3, 4])


if __name__ == '__main__':
    test()
