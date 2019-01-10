#!/usr/bin/env python
"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Created on 2018-12-29

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""

from list_node import *


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = tmp = itor = head
        tmp_len = 0
        while itor:
            if tmp_len < n + 1:
                tmp_len += 1
            else:
                tmp = tmp.next
            itor = itor.next
        if l == tmp and tmp_len == n:
            if l.next:
                return l.next
            else:
                return []
        if tmp and tmp.next:
            tmp.next = tmp.next.next
        else:
            return []
        return l


if __name__ == '__main__':
    assert Solution().removeNthFromEnd(buildListNode([1, 2, 3]), 2) == buildListNode([1, 3])
    assert Solution().removeNthFromEnd(buildListNode([1, 2, 3, 4, 5]), 2) == buildListNode([1, 2, 3, 5])
    assert Solution().removeNthFromEnd(buildListNode([1, 2, 3, 4, 5]), 5) == buildListNode([2, 3, 4, 5])
    assert Solution().removeNthFromEnd(buildListNode([1, 2, 3, 4, 5]), 1) == buildListNode([1, 2, 3, 4])
    assert Solution().removeNthFromEnd(buildListNode([1]), 1) == []
    assert Solution().removeNthFromEnd(buildListNode([1, 2]), 2) == buildListNode([2])
    assert Solution().removeNthFromEnd(buildListNode([1, 2]), 1) == buildListNode([1])
