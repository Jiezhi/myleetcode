#!/usr/bin/env python
"""
CREATED AT: 2021/10/31
Des:

https://leetcode.com/contest/weekly-contest-265/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
from typing import Optional, List

from list_node import ListNode, buildListNode


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """
        The number of nodes in the list is in the range [2, 10^5].
        1 <= Node.val <= 10^5
        :param head:
        :return:
        """
        critical = []
        pos = 1
        while head is not None and head.next is not None and head.next.next is not None:
            if head.val < head.next.val > head.next.next.val or head.val > head.next.val < head.next.next.val:
                critical.append(pos)
            head = head.next
            pos += 1
        if len(critical) <= 1:
            return [-1, -1]
        ret_min = pos
        ret_max = critical[-1] - critical[0]
        for i in range(1, len(critical)):
            ret = critical[i] - critical[i - 1]
            if ret < ret_min:
                ret_min = ret
        return [ret_min, ret_max]


def test():
    assert Solution().nodesBetweenCriticalPoints(head=buildListNode([3, 1])) == [-1, -1]
    assert Solution().nodesBetweenCriticalPoints(head=buildListNode([1, 3, 2, 2, 3, 2, 2, 2, 7])) == [3, 3]
    assert Solution().nodesBetweenCriticalPoints(head=buildListNode([5, 3, 1, 2, 5, 1, 2])) == [1, 3]


if __name__ == '__main__':
    test()
