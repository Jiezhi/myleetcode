#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-07-29

Leetcode: https://leetcode.com/problems/reverse-linked-list/

"""
from list_node import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        tmp = None
        while cur:
            cur_list = cur.next
            cur.next = tmp
            tmp = cur
            cur = cur_list

        return tmp


def test():
    assert Solution().reverseList(buildListNode([])) == buildListNode([])
    assert Solution().reverseList(buildListNode([1, 2, 3, 4, 5])) == buildListNode([5, 4, 3, 2, 1])


if __name__ == '__main__':
    test()
