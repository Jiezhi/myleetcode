#!/usr/bin/env python3
"""
CREATED AT: 2022-10-12

URL: https://leetcode.com/problems/linked-list-components/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 817-LinkedListComponents

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from list_node import ListNode
from tool import *


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        """
        Runtime: 107 ms, faster than 97.96%
        Memory Usage: 19.3 MB, less than 23.36%

        The number of nodes in the linked list is n.
        1 <= n <= 10^4
        0 <= Node.val < n
        All the values Node.val are unique.
        1 <= nums.length <= n
        0 <= nums[i] < n
        All the values of nums are unique.
        """
        nums = set(nums)
        ret = 0
        pre = False
        while head:
            if head.val in nums:
                if not pre:
                    pre = True
                    ret += 1
            else:
                pre = False
            head = head.next
        return ret


def test():
    assert Solution().numComponents(head=ListNode.from_list([0, 1, 2, 3]), nums=[0, 1, 3]) == 2
    assert Solution().numComponents(head=ListNode.from_list([0, 1, 2, 3, 4]), nums=[0, 3, 1, 4]) == 2


if __name__ == '__main__':
    test()
