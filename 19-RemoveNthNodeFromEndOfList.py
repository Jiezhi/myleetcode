#!/usr/bin/env python
"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/603/
Created on 2018-12-29

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
from typing import Optional

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

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Hint: Maintain two pointers and update one with a delay of n steps.

        208 / 208 test cases passed.
        Status: Accepted
        Runtime: 24 ms
        Memory Usage: 14.3 MB

        :param self:
        :param head:
        :param n:
        :return:
        """
        first_point = head
        second_point = head
        # let the first point go n farther!
        for _ in range(n):
            first_point = first_point.next
        # first point reach the end, means we need to delete the first node
        if not first_point:
            return head.next
        # go together, second point always behind the first point n steps
        while first_point and first_point.next:
            first_point = first_point.next
            second_point = second_point.next
        second_point.next = second_point.next.next
        return head


def test():
    assert Solution().removeNthFromEnd2(buildListNode([1, 2, 3]), 2) == buildListNode([1, 3])
    assert Solution().removeNthFromEnd2(buildListNode([1, 2, 3, 4, 5]), 2) == buildListNode([1, 2, 3, 5])
    assert Solution().removeNthFromEnd2(buildListNode([1, 2, 3, 4, 5]), 5) == buildListNode([2, 3, 4, 5])
    assert Solution().removeNthFromEnd2(buildListNode([1, 2, 3, 4, 5]), 1) == buildListNode([1, 2, 3, 4])
    assert Solution().removeNthFromEnd2(buildListNode([1]), 1) is None
    assert Solution().removeNthFromEnd2(buildListNode([1, 2]), 2) == buildListNode([2])
    assert Solution().removeNthFromEnd2(buildListNode([1, 2]), 1) == buildListNode([1])

    assert Solution().removeNthFromEnd(buildListNode([1, 2, 3]), 2) == buildListNode([1, 3])
    assert Solution().removeNthFromEnd(buildListNode([1, 2, 3, 4, 5]), 2) == buildListNode([1, 2, 3, 5])
    assert Solution().removeNthFromEnd(buildListNode([1, 2, 3, 4, 5]), 5) == buildListNode([2, 3, 4, 5])
    assert Solution().removeNthFromEnd(buildListNode([1, 2, 3, 4, 5]), 1) == buildListNode([1, 2, 3, 4])
    assert Solution().removeNthFromEnd(buildListNode([1]), 1) == []
    assert Solution().removeNthFromEnd(buildListNode([1, 2]), 2) == buildListNode([2])
    assert Solution().removeNthFromEnd(buildListNode([1, 2]), 1) == buildListNode([1])


if __name__ == '__main__':
    test()
