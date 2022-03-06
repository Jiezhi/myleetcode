#!/usr/bin/env python
"""
CREATED AT: 2022/3/6
Des:

https://leetcode.com/problems/sort-the-jumbled-numbers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from functools import lru_cache
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        mapping.length == 10
        0 <= mapping[i] <= 9
        All the values of mapping[i] are unique.
        1 <= nums.length <= 3 * 10^4
        0 <= nums[i] < 10^9
        """

        @lru_cache(None)
        def convert(num) -> int:
            if num == 0:
                return mapping[0]
            ret = 0
            m = 1
            while num:
                num, left = divmod(num, 10)
                ret += mapping[left] * m
                m *= 10
            return ret

        num_map = [(convert(x), x) for x in nums]

        return [x[1] for x in sorted(num_map, key=lambda x: x[0])]


def test():
    assert Solution().sortJumbled(mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]) == [338, 38, 991]
    assert Solution().sortJumbled(mapping=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums=[123, 456, 789]) == [123, 456, 789]


if __name__ == '__main__':
    test()
