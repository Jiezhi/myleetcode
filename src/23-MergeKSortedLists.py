#!/usr/bin/env python
"""
CREATED AT: 2022/3/3
Des:

https://leetcode.com/problems/merge-k-sorted-lists/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

Time Spent:  min
"""

from typing import List, Optional

from src.list_node import ListNode, buildListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        k == lists.length
        0 <= k <= 10^4
        0 <= lists[i].length <= 500
        -10^4 <= lists[i][j] <= 10^4
        lists[i] is sorted in ascending order.
        The sum of lists[i].length will not exceed 10^4.
        """
        if not lists:
            return None

        def merge(lists1: List, lists2: List) -> Optional[ListNode]:
            if not lists1:
                return lists2
            if not lists2:
                return lists1
            if len(lists1) > 1:
                n = len(lists1)
                node1 = merge(lists1[:n // 2], lists1[n // 2:])
            else:
                node1 = lists1[0]

            if len(lists2) > 1:
                n = len(lists2)
                node2 = merge(lists2[:n // 2], lists2[n // 2:])
            else:
                node2 = lists2[0]

            # merge two single list
            head = ListNode(0)
            node = head
            while node1 and node2:
                if node1.val <= node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                node = node.next
            if node1:
                node.next = node1
            if node2:
                node.next = node2
            return head.next

        n = len(lists)
        if n == 1:
            return lists[0]
        return merge(lists[:n // 2], lists[n // 2:])


def test():
    assert Solution().mergeKLists([]) is None
    assert Solution().mergeKLists([[]]) == []
    assert Solution().mergeKLists(
        lists=[
            buildListNode([1, 4, 5]),
            buildListNode([1, 3, 4]),
            buildListNode([2, 6])
        ]) == buildListNode([1, 1, 2, 3, 4, 4, 5, 6])


if __name__ == '__main__':
    test()
