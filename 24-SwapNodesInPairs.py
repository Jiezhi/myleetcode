#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-07-29

Leetcode: https://leetcode.com/problems/swap-nodes-in-pairs/

"""
from list_node import ListNode, buildListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ret = tmp = self
        tmp.next = head
        while tmp.next and tmp.next.next:
            left = tmp.next
            right = left.next
            tmp.next, right.next, left.next = right, left, right.next
            # tmp.next = right
            # right.next = left
            # left.next = right.next
            tmp = left

        return ret.next


def test():
    assert Solution().swapPairs(buildListNode([1, 2, 3, 4])) == buildListNode([2, 1, 4, 3])


if __name__ == '__main__':
    test()
