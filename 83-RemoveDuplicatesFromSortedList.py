#!/usr/bin/env python
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
Created on 2018-11-16

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""

from list_node import *


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        ret = last = head
        head = head.next
        while head:
            if last.val == head.val:
                head = last.next = head.next
            else:
                last = head
                head = head.next
        return ret


def test():
    assert Solution().deleteDuplicates(buildListNode([])) == buildListNode([])
    assert Solution().deleteDuplicates(buildListNode([1, 1, 2])) == buildListNode([1, 2])
    assert Solution().deleteDuplicates(buildListNode([1, 1, 2, 3, 3])) == buildListNode([1, 2, 3])
