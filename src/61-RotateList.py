#!/usr/bin/env python
"""
CREATED AT: 2021/12/6
Des:

https://leetcode.com/problems/rotate-list/
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: ListNode

See: 
"""

from typing import Optional

from list_node import ListNode, buildListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Runtime: 36 ms, faster than 77.75% of Python3
        Memory Usage: 14.2 MB, less than 86.24% of Python3
        The number of nodes in the list is in the range [0, 500].
        -100 <= Node.val <= 100
        0 <= k <= 2 * 10^9
        :param head:
        :param k:
        :return:
        """
        if head is None:
            return None
        l = 1
        node = head
        while node.next is not None:
            l += 1
            node = node.next
        tail = node
        k = k % l
        if k == 0:
            return head
        k = l - k - 1
        i = 0
        node = head
        while i < k:
            node = node.next
            i += 1
        new_head = node.next
        node.next = None
        tail.next = head
        return new_head


def test():
    assert Solution().rotateRight(head=buildListNode([1, 2, 3, 4, 5]), k=2) == buildListNode([4, 5, 1, 2, 3])
    assert Solution().rotateRight(head=buildListNode([0, 1, 2]), k=4) == buildListNode([2, 0, 1])
    assert Solution().rotateRight(head=buildListNode([0, 1, 2]), k=0) == buildListNode([0, 1, 2])
    assert Solution().rotateRight(head=buildListNode([0, 1, 2]), k=3) == buildListNode([0, 1, 2])
    assert Solution().rotateRight(head=buildListNode([]), k=3) == buildListNode([])


if __name__ == '__main__':
    test()
