#!/usr/bin/env python
"""
CREATED AT: 2022/2/24
Des:

https://leetcode.com/problems/sort-list/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import Optional

from src.list_node import ListNode, buildListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 169 ms, faster than 97.42%
        Memory Usage: 30 MB, less than 71.51%

        The number of nodes in the list is in the range [0, 5 * 10^4].
        -10^5 <= Node.val <= 10^5
        """
        if not head:
            return head
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        nums = sorted(nums)
        node = head
        for num in nums:
            node.val = num
            node = node.next
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        TLE
        The number of nodes in the list is in the range [0, 5 * 10^4].
        -10^5 <= Node.val <= 10^5
        """
        if not head:
            return head
        pre_node = head
        while pre_node and pre_node.next:
            curr_node = pre_node.next
            if curr_node.val < pre_node.val:
                if curr_node.val <= head.val:
                    pre_node.next = curr_node.next
                    curr_node.next = head
                    head = curr_node
                else:
                    node = head
                    while not node.val <= curr_node.val <= node.next.val:
                        node = node.next
                    # insert after node
                    pre_node.next = curr_node.next
                    curr_node.next = node.next
                    node.next = curr_node
            else:
                pre_node = curr_node
        return head


def test():
    assert Solution().sortList(head=buildListNode([4, 2, 1, 3])) == buildListNode([1, 2, 3, 4])


if __name__ == '__main__':
    test()
