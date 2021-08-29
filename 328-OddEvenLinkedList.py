#!/usr/bin/env python
"""
CREATED AT: 2021/8/28
Des:
https://leetcode.com/problems/odd-even-linked-list/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/
GITHUB: https://github.com/Jiezhi/myleetcode

"""

from typing import Optional

from list_node import ListNode, buildListNode, printData


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        70 / 70 test cases passed.
        Status: Accepted
        Runtime: 40 ms
        Memory Usage: 16.4 MB
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head
        odd_list, odd_tmp = head, head
        even_list, even_tmp = head.next, head.next
        odd = True
        node = head.next.next
        while node is not None:
            if odd:
                odd_tmp.next = node
                odd_tmp = odd_tmp.next
                odd = False
            else:
                even_tmp.next = node
                even_tmp = even_tmp.next
                odd = True
            node = node.next
        even_tmp.next = None
        odd_tmp.next = even_list
        return odd_list


def test():
    assert Solution().oddEvenList(head=buildListNode([])) == buildListNode([])
    assert Solution().oddEvenList(head=buildListNode([1])) == buildListNode([1])
    assert Solution().oddEvenList(head=buildListNode([1, 2])) == buildListNode([1, 2])
    assert Solution().oddEvenList(head=buildListNode([1, 2, 3])) == buildListNode([1, 3, 2])
    assert Solution().oddEvenList(head=buildListNode([1, 2, 3, 4, 5])) == buildListNode([1, 3, 5, 2, 4])
    assert Solution().oddEvenList(head=buildListNode([2, 1, 3, 5, 6, 4, 7])) == buildListNode([2, 3, 6, 7, 1, 5, 4])


if __name__ == '__main__':
    test()
