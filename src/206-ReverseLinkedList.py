#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-07-29
Updated on 2021-09-07

Leetcode: https://leetcode.com/problems/reverse-linked-list/
https://leetcode.com/explore/item/3966
Difficulty: Easy
"""
from list_node import ListNode
from tool import *


class Solution:
    @print_results
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        20210907 Updated with recursively
        28 / 28 test cases passed.
        Status: Accepted
        Runtime: 40 ms
        Memory Usage: 20.3 MB
        :param head:
        :return:
        """

        def reverse(nl: ListNode):
            if nl is None or nl.next is None:
                return nl, nl
            hnode, tnode = reverse(nl.next)
            nl.next = None
            tnode.next = nl
            return hnode, nl

        ret, _ = reverse(head)
        return ret

    def reverseList(self, head: ListNode) -> ListNode:
        """
        2022-08-23
        :param head:
        :return:
        """
        pre = None
        while head:
            pre, head.next, head = head, pre, head.next
        return pre


def test():
    assert Solution().reverseList2(ListNode.from_list([])) == ListNode.from_list([])
    assert Solution().reverseList2(ListNode.from_list([1, 2, 3, 4, 5])) == ListNode.from_list([5, 4, 3, 2, 1])

    assert Solution().reverseList(ListNode.from_list([])) == ListNode.from_list([])
    assert Solution().reverseList(ListNode.from_list([1, 2, 3, 4, 5])) == ListNode.from_list([5, 4, 3, 2, 1])


if __name__ == '__main__':
    test()
