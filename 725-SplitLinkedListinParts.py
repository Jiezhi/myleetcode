#!/usr/bin/env python
"""
CREATED AT: 2021/9/29
Des:
https://leetcode.com/problems/split-linked-list-in-parts
https://leetcode.com/explore/item/3992
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium


"""

from typing import Optional, List

from list_node import ListNode, buildListNode
from tool import print_results


class Solution:
    @print_results
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """
        43 / 43 test cases passed.
        Status: Accepted
        Runtime: 40 ms
        Memory Usage: 14.9 MB
        :param head:
        :param k:
        :return:
        """
        n = 0
        ret = []
        tmp_node = head
        while tmp_node is not None:
            n += 1
            tmp_node = tmp_node.next
        n, l = divmod(n, k)
        for i in range(k):
            if head is None:
                ret.append(None)
                continue
            tmp_head = ListNode(0)
            tmp_node = tmp_head
            for j in range(n):
                if head is None:
                    break
                tmp_node.next = ListNode(head.val)
                tmp_node = tmp_node.next
                head = head.next
            if l > 0 and head is not None:
                tmp_node.next = ListNode(head.val)
                head = head.next
                l -= 1
            ret.append(tmp_head.next)
        return ret


def test():
    assert Solution().splitListToParts(
        head=buildListNode([1, 2, 3]), k=5) == [
               buildListNode([1]), buildListNode([2]), buildListNode([3])
               , buildListNode([]), buildListNode([])]
    assert Solution().splitListToParts(
        head=buildListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), k=3
    ) == [buildListNode([1, 2, 3, 4]),
          buildListNode([5, 6, 7]),
          buildListNode([8, 9, 10])]


if __name__ == '__main__':
    test()
