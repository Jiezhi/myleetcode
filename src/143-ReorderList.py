#!/usr/bin/env python
"""
CREATED AT: 2021/12/22
Des:

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 20 min
"""
from typing import Optional

from list_node import ListNode, buildListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Runtime: 96 ms, faster than 53.19%
        Memory Usage: 23.2 MB, less than 94.94%

        Do not return anything, modify head in-place instead.
        The number of nodes in the list is in the range [1, 5 * 10^4].
        1 <= Node.val <= 1000
        """
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next
        node = head.next
        index = 1
        flag = 1
        while index <= len(nums) / 2 and node:
            flag *= -1
            node.val = nums[index * flag]
            node = node.next
            if flag == 1:
                index += 1


def test():
    test_case = buildListNode([1])
    Solution().reorderList(test_case)
    assert test_case == buildListNode([1])

    test_case = buildListNode([1, 2])
    Solution().reorderList(test_case)
    assert test_case == buildListNode([1, 2])

    test_case = buildListNode([1, 2, 3])
    Solution().reorderList(test_case)
    assert test_case == buildListNode([1, 3, 2])

    test_case = buildListNode([1, 2, 3, 4])
    Solution().reorderList(test_case)
    assert test_case == buildListNode([1, 4, 2, 3])

    test_case = buildListNode([1, 2, 3, 4, 5])
    Solution().reorderList(test_case)
    assert test_case == buildListNode([1, 5, 2, 4, 3])


if __name__ == '__main__':
    test()
