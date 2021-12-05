#!/usr/bin/env python
"""
CREATED AT: 2021/12/5
Des:

https://leetcode.com/contest/weekly-contest-270/problems/delete-the-middle-node-of-a-linked-list/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""
from typing import Optional

from src.list_node import ListNode, buildListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        The number of nodes in the list is in the range [1, 10^5].
        1 <= Node.val <= 10^5
        :param head:
        :return:
        """
        l = 0
        node = head
        while node is not None:
            l += 1
            node = node.next
        pre_mid = l // 2 - 1
        if pre_mid < 0:
            return head.next
        node = head
        while pre_mid > 0:
            node = node.next
            pre_mid -= 1
        node.next = node.next.next
        return head


def test():
    assert Solution().deleteMiddle(head=buildListNode([1, 3, 4, 7, 1, 2, 6])) == buildListNode([1, 3, 4, 1, 2, 6])
    assert Solution().deleteMiddle(head=buildListNode([1, 2, 3, 4])) == buildListNode([1, 2, 4])
    assert Solution().deleteMiddle(head=buildListNode([1, 2, 3])) == buildListNode([1, 3])
    assert Solution().deleteMiddle(head=buildListNode([2, 1])) == buildListNode([2])
    assert Solution().deleteMiddle(head=buildListNode([2])) == buildListNode([])


if __name__ == '__main__':
    test()
