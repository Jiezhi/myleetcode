#!/usr/bin/env python
"""
CREATED AT: 2022/1/7
Des:

https://leetcode.com/problems/linked-list-random-node/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Ref: https://leetcode.com/problems/linked-list-random-node/solution/
https://leetcode.com/problems/linked-list-random-node/solution/

Time Spent:  min
"""

import random
from typing import Optional

from list_node import ListNode, buildListNode


class Solution:
    """
    Runtime: 144 ms, faster than 29.63%
    Memory Usage: 17.4 MB, less than 23.25%

    The number of nodes in the linked list will be in the range [1, 10^4].
    -10^4 <= Node.val <= 10^4
    At most 10^4 calls will be made to getRandom.
    """

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        if not self.head:
            return None
        k = 1
        curr = self.head

        while curr:
            if random.random() < 1 / k:
                ret = curr.val
            curr = curr.next
            k += 1
        return ret


def test():
    nums = [1, 2, 3]
    solution = Solution(head=buildListNode(nums))
    assert solution.getRandom() in nums
    assert solution.getRandom() in nums
    assert solution.getRandom() in nums


if __name__ == '__main__':
    test()
