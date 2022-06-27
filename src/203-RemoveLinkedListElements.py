#!/usr/bin/env python
"""
CREATED AT: 2021/12/1
Des:

https://leetcode.com/problems/remove-linked-list-elements/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""
from typing import Optional

from list_node import ListNode, buildListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        66 / 66 test cases passed.
        Status: Accepted
        Runtime: 72 ms
        Memory Usage: 17.2 MB
        The number of nodes in the list is in the range [0, 10^4].
        1 <= Node.val <= 50
        0 <= val <= 50
        :param head:
        :param val:
        :return:
        """
        while head is not None and head.val == val:
            head = head.next
        node = head
        while node is not None and node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head


def test():
    assert Solution().removeElements(head=buildListNode([1, 2, 6, 3, 4, 5, 6]), val=6) == buildListNode([1, 2, 3, 4, 5])
    assert Solution().removeElements(head=buildListNode([]), val=6) == buildListNode([])
    assert Solution().removeElements(head=buildListNode([7, 7, 7, 7]), val=7) == buildListNode([])
    assert Solution().removeElements(head=buildListNode([1, 7, 7, 7, 7, 1]), val=7) == buildListNode([1, 1])


if __name__ == '__main__':
    test()
