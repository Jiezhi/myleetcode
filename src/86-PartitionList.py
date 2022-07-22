#!/usr/bin/env python3
"""
CREATED AT: 2022-07-22

URL: https://leetcode.com/problems/partition-list/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 86-PartitionList

Difficulty: Medium

Desc: 

Tag: 

See: 

"""

from list_node import ListNode
from tool import *


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        Runtime: 55 ms, faster than 47.20%
        Memory Usage: 13.8 MB, less than 98.64%
        The number of nodes in the list is in the range [0, 200].
        -100 <= Node.val <= 100
        -200 <= x <= 200
        """
        if not head:
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        pre, cur = sentinel, head
        while cur and cur.val < x:
            pre = cur
            cur = cur.next
        while cur and cur.next:
            if cur.next.val >= x:
                cur = cur.next
            else:
                nxt = cur.next.next
                cur.next.next = pre.next
                pre.next = cur.next
                cur.next = nxt
                pre = pre.next

        return sentinel.next


def test():
    assert Solution().partition(head=ListNode.from_list([1, 4, 3, 2, 5, 2]), x=3) == ListNode.from_list(
        [1, 2, 2, 4, 3, 5])
    assert Solution().partition(head=ListNode.from_list([4, 3, 2, 5, 2]), x=3) == ListNode.from_list([2, 2, 4, 3, 5])
    assert Solution().partition(head=ListNode.from_list([2, 1]), x=2) == ListNode.from_list([1, 2])
    assert Solution().partition(head=ListNode.from_list([]), x=2) == ListNode.from_list([])
    assert Solution().partition(head=ListNode.from_list([1, 4, 3, 0, 2, 5, 2]), x=3) == ListNode.from_list(
        [1, 0, 2, 2, 4, 3, 5])
    assert Solution().partition(head=ListNode.from_list([1, 1, 2]), x=2) == ListNode.from_list([1, 1, 2])


if __name__ == '__main__':
    test()
