#!/usr/bin/env python
"""
CREATED AT: 2022/3/22
Des:
https://leetcode.com/problems/reverse-nodes-in-k-group/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""

from typing import Optional

from list_node import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Runtime: 91 ms, faster than 19.00%
        Memory Usage: 15.9 MB, less than 5.48%

        The number of nodes in the list is n.
        1 <= k <= n <= 5000
        0 <= Node.val <= 1000
        """
        if k == 1:
            return head

        def reverse(head) -> Optional[ListNode]:
            pre = None
            while head:
                pre, head.next, head = head, pre, head.next
            return pre

        sentinal = ListNode(0, head)
        tail = sentinal

        tmp_node = head

        i = 1
        while tmp_node:
            if i == k:
                next_head = tmp_node.next
                tmp_node.next = None
                ret = reverse(head)
                tail.next = ret
                tail = head
                i = 1
                tmp_node = next_head
                head = next_head
            else:
                tmp_node = tmp_node.next
                i += 1
        if head:
            tail.next = head
        return sentinal.next


def test():
    assert Solution().reverseKGroup(ListNode.from_list([1, 2, 3, 4, 5]), 2) == ListNode.from_list([2, 1, 4, 3, 5])


if __name__ == '__main__':
    test()
