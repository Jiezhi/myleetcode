#!/usr/bin/env python3
"""
CREATED AT: 2022-07-21

URL: https://leetcode.com/problems/reverse-linked-list-ii/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 92-ReverseLinkedListII

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from typing import Optional

from list_node import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Runtime: 53 ms, faster than 38.31% 
        Memory Usage: 14.1 MB, less than 51.75% 

        The number of nodes in the list is n.
        1 <= n <= 500
        -500 <= Node.val <= 500
        1 <= left <= right <= n
        """
        if left == right:
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        pos, first = 0, sentinel
        while pos < left - 1:
            first = first.next
            pos += 1
        # reverse from first's next node
        pre, cur = first, first.next
        while pos < right:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
            pos += 1
        first.next.next = cur
        first.next = pre

        return sentinel.next


def test():
    assert Solution().reverseBetween(head=ListNode.from_list([1, 2, 3, 4, 5]), left=2, right=4) == ListNode.from_list(
        [1, 4, 3, 2, 5])
    assert Solution().reverseBetween(head=ListNode.from_list([1, 2, 3, 4, 5]), left=1, right=5) == ListNode.from_list(
        [5, 4, 3, 2, 1])
    assert Solution().reverseBetween(head=ListNode.from_list([1, 2, 3, 4, 5]), left=1, right=4) == ListNode.from_list(
        [4, 3, 2, 1, 5])
    assert Solution().reverseBetween(head=ListNode.from_list([5]), left=1, right=1) == ListNode.from_list([5])


if __name__ == '__main__':
    test()
