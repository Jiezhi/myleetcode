#!/usr/bin/env python
"""
CREATED AT: 2022/6/1
Des:
https://leetcode.com/problems/running-sum-of-1d-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
import itertools
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Runtime: 51 ms, faster than 63.27%
        Memory Usage: 14 MB, less than 73.38%
        1 <= nums.length <= 1000
        -10^6 <= nums[i] <= 10^6
        :param nums:
        :return:
        """
        return list(itertools.accumulate(nums))


def test():
    assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]


if __name__ == '__main__':
    test()
