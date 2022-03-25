#!/usr/bin/env python
"""
CREATED AT: 2022/3/25
Des:
https://leetcode.com/problems/largest-perimeter-triangle/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Runtime: 371 ms, faster than 10.98%
        Memory Usage: 15.4 MB, less than 50.75%

        :param nums: 3 <= nums.length <= 10^4
                     1 <= nums[i] <= 10^6
        :return:
        """
        nums = sorted(nums, reverse=True)

        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


def test():
    assert Solution().largestPerimeter([2, 1, 2]) == 5


if __name__ == '__main__':
    test()
