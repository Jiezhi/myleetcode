#!/usr/bin/env python
"""
CREATED AT: 2021/12/28
Des:

https://leetcode.com/problems/middle-of-the-linked-list/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See:

Ref: https://leetcode.com/problems/middle-of-the-linked-list/solution/

Time Spent:  min
"""
from typing import Optional

from src.list_node import ListNode, buildListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 32 ms, faster than 60.47%
        Memory Usage: 14.2 MB, less than 46.38%
        The number of nodes in the list is in the range [1, 100].
        1 <= Node.val <= 100
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 24 ms, faster than 95.40%
        Memory Usage: 14.3 MB, less than 46.38%
        The number of nodes in the list is in the range [1, 100].
        1 <= Node.val <= 100
        :param head:
        :return:
        """
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        length = length // 2
        node = head
        while length > 0:
            node = node.next
            length -= 1
        return node


def test():
    assert Solution().middleNode(head=buildListNode([1])) == buildListNode([1])
    assert Solution().middleNode(head=buildListNode([1, 2])) == buildListNode([2])
    assert Solution().middleNode(head=buildListNode([1, 2, 3, 4, 5])) == buildListNode([3, 4, 5])
    assert Solution().middleNode(head=buildListNode([1, 2, 3, 4, 5, 6])) == buildListNode([4, 5, 6])


if __name__ == '__main__':
    test()
