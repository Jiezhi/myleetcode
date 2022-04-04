#!/usr/bin/env python
"""
CREATED AT: 2022/4/4
Des:
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""

from typing import Optional

from src.list_node import ListNode


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Runtime: 1587 ms, faster than 31.65%
        Memory Usage: 48.4 MB, less than 85.24%

        The number of nodes in the list is n.
        1 <= k <= n <= 10^5
        0 <= Node.val <= 100
        """
        fast = head
        cnt = 1
        while cnt < k:
            fast = fast.next
            cnt += 1
        left = fast
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.val, left.val = left.val, slow.val
        return head


def test():
    assert Solution().swapNodes(ListNode.from_list([1, 2, 3, 4, 5]), 2) == ListNode.from_list([1, 4, 3, 2, 5])


if __name__ == '__main__':
    test()
