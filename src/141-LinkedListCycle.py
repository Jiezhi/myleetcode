#!/usr/bin/env python
"""
Created on 20210722

Des:
https://leetcode.com/problems/linked-list-cycle/
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

Reference: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1211/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from list_node import ListNode, buildListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slower_pointer = head
        faster_pointer = head.next
        while faster_pointer and faster_pointer.next and slower_pointer != faster_pointer:
            slower_pointer = slower_pointer.next
            faster_pointer = faster_pointer.next.next

        if slower_pointer == faster_pointer:
            return True
        else:
            return False


def test():
    # It's hard to build a cycle list node using my ListNode class, so just test yourself.
    assert not Solution().hasCycle(buildListNode([1]))


if __name__ == '__main__':
    test()
