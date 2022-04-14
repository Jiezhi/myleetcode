#!/usr/bin/env python
"""
CREATED AT: 2022/1/8
Des:

https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
https://leetcode.com/contest/biweekly-contest-69/problems/maximum-twin-sum-of-a-linked-list/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""

from typing import Optional

from src.list_node import ListNode, buildListNode


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        The number of nodes in the list is an even integer in the range [2, 10^5].
        1 <= Node.val <= 10^5
        :param head:
        :return:
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        n = len(nums)
        return max(nums[x] + nums[n - x - 1] for x in range(n // 2))


def test():
    assert Solution().pairSum(head=buildListNode([5, 4, 2, 1])) == 6
    assert Solution().pairSum(head=buildListNode([4, 2, 2, 3])) == 7
    assert Solution().pairSum(head=buildListNode([1, 100000])) == 100001


if __name__ == '__main__':
    test()
