#!/usr/bin/env python
"""
CREATED AT: 2021/12/15
Des:

https://leetcode.com/problems/insertion-sort-list/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 10 min

Nodes:
It might be faster to copy the value to array, and sort the value in the array, then build listnode on the sorted array.
https://stackoverflow.com/questions/1525117/whats-the-fastest-algorithm-for-sorting-a-linked-list/1525419#1525419
http://steve-yegge.blogspot.com/2008/03/get-that-job-at-google.html
"""
from typing import Optional

from src.list_node import ListNode, buildListNode


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 1555 ms, faster than 55.68%
        Memory Usage: 17.4 MB, less than 7.76% of Python3

        The number of nodes in the list is in the range [1, 5000].
        -5000 <= Node.val <= 5000
        :param head:
        :return:
        """
        if not head:
            return None
        ret = ListNode(head.val)
        node = head.next
        while node:
            tmp_node = ret
            if node.val <= tmp_node.val:
                ret = ListNode(node.val)
                ret.next = tmp_node
            else:
                while tmp_node.next and node.val > tmp_node.next.val:
                    tmp_node = tmp_node.next
                tmp = ListNode(node.val)
                tmp.next = tmp_node.next
                tmp_node.next = tmp
            node = node.next
        return ret


def test():
    assert Solution().insertionSortList(buildListNode([4])) == buildListNode([4])
    assert Solution().insertionSortList(buildListNode([4, 0])) == buildListNode([0, 4])
    assert Solution().insertionSortList(buildListNode([4, 2, 1, 3])) == buildListNode([1, 2, 3, 4])
    assert Solution().insertionSortList(buildListNode([-1, 5, 3, 4, 0])) == buildListNode([-1, 0, 3, 4, 5])


if __name__ == '__main__':
    test()
