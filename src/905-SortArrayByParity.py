#!/usr/bin/env python
"""
CREATED AT: 2022/4/28
Des:
https://leetcode.com/problems/sort-array-by-parity/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Runtime: 119 ms, faster than 36.32%
        Memory Usage: 14.7 MB, less than 18.14%

        1 <= nums.length <= 5000
        0 <= nums[i] <= 5000
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            while lo < hi and nums[lo] & 1 == 0:
                lo += 1
            while lo < hi and nums[hi] & 1 == 1:
                hi -= 1
            if lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        return nums


def test():
    assert Solution().sortArrayByParity([3, 1, 2, 4]) == [4, 2, 1, 3]


if __name__ == '__main__':
    test()
