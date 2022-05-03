#!/usr/bin/env python
"""
CREATED AT: 2022/5/3
Des:
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Runtime: 267 ms, faster than 56.59%
        Memory Usage: 15.3 MB, less than 20.50%

        1 <= nums.length <= 10^4
        -10^5 <= nums[i] <= 10^5
        """
        new_nums = sorted(nums)
        lo, hi = 0, len(nums) - 1
        while lo <= hi and nums[lo] == new_nums[lo]:
            lo += 1
        while lo <= hi and nums[hi] == new_nums[hi]:
            hi -= 1

        return hi - lo + 1


def test():
    assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert Solution().findUnsortedSubarray([1, 2, 3, 4]) == 0


if __name__ == '__main__':
    test()
