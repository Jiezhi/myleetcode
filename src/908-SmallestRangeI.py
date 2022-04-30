#!/usr/bin/env python
"""
CREATED AT: 2022/4/30
Des:
https://leetcode.com/problems/smallest-range-i/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        """
        Runtime: 191 ms, faster than 24.90%
        Memory Usage: 15.5 MB, less than 19.14%

        :param nums:
        :param k:
        :return:
        """
        return max(0, max(nums) - min(nums) - 2 * k)


def test():
    assert Solution().smallestRangeI(nums=[1], k=0) == 0


if __name__ == '__main__':
    test()
