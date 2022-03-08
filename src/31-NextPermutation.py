#!/usr/bin/env python
"""
CREATED AT: 2022/3/8
Des:

https://leetcode.com/problems/next-permutation/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Runtime: 80 ms, faster than 14.83%
        Memory Usage: 14 MB, less than 53.79%

        Do not return anything, modify nums in-place instead.
        1 <= nums.length <= 100
        0 <= nums[i] <= 100
        """

        def swap(lo, hi):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        hi = len(nums) - 1
        while hi > 0 and nums[hi - 1] >= nums[hi]:
            hi -= 1

        if hi == 0:
            swap(0, len(nums) - 1)
            return
        pos_to_swap = hi - 1
        value = nums[hi - 1]
        hi = len(nums) - 1
        while hi > 0 and value >= nums[hi]:
            hi -= 1
        nums[pos_to_swap], nums[hi] = nums[hi], nums[pos_to_swap]

        lo, hi = pos_to_swap + 1, len(nums) - 1
        swap(lo, hi)


def test():
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    assert nums == [1, 3, 2]
    
    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    assert nums == [1, 2, 3]


if __name__ == '__main__':
    test()
