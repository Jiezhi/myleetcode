#!/usr/bin/env python
"""
CREATED AT: 2022/2/20
Des:

https://leetcode.com/problems/merge-nodes-in-between-zeros/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import Optional

from list_node import ListNode, buildListNode


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        39 / 39 test cases passed.
        Status: Accepted
        Runtime: 5028 ms
        Memory Usage: 72.9 MB
        Submitted: 7 hours, 5 minutes ago

        The number of nodes in the list is in the range [3, 2 * 10^5].
        0 <= Node.val <= 1000
        There are no two consecutive nodes with Node.val == 0.
        The beginning and end of the linked list have Node.val == 0.
        """
        curr_head = head
        curr_end = head.next
        ret = 0
        while curr_end:
            if curr_end.val != 0:
                ret += curr_end.val
            else:
                # curr_end at the num end next node : 0
                curr_head.val = ret
                ret = 0
                if not curr_end.next:
                    curr_head.next = None
                    break
                curr_head.next = curr_end
                curr_head = curr_end
            curr_end = curr_end.next
        return head


def test():
    assert Solution().mergeNodes(buildListNode([0, 3, 1, 0, 4, 5, 2, 0])) == buildListNode([4, 11])


if __name__ == '__main__':
    test()
