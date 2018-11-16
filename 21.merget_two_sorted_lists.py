#!/usr/bin/env python
"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
Created on 2018-11-11

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""

from list_node import *


class Solution:
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


if __name__ == '__main__':
    assert Solution().mergeTwoLists(buildListNode([1, 2, 3]), buildListNode([2, 3, 4])) \
           == buildListNode([1, 2, 2, 3, 3, 4])
