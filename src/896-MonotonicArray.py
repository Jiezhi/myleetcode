#!/usr/bin/env python3
"""
CREATED AT: 2022-06-13

URL: https://leetcode.com/problems/monotonic-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 896-MonotonicArray

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Runtime: 1322 ms, faster than 49.51% 
        Memory Usage: 28 MB, less than 62.25% 

        1 <= nums.length <= 10^5
        -105 <= nums[i] <= 10^5
        """
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)


def test():
    assert Solution().isMonotonic(nums=[1, 2, 2, 3])
    assert not Solution().isMonotonic(nums=[1, 3, 2, 3])


if __name__ == '__main__':
    test()

