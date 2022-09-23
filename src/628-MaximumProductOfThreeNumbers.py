#!/usr/bin/env python3
"""
CREATED AT: 2022-09-23

URL: https://leetcode.com/problems/maximum-product-of-three-numbers

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 628-MaximumProductOfThreeNumbers

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Runtime: 692 ms, faster than 5.49%
        Memory Usage: 15.2 MB, less than 22.80%
        3 <= nums.length <= 10^4
        -1000 <= nums[i] <= 1000
        """
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


def test():
    assert Solution().maximumProduct(nums=[1, 2, 3]) == 6
    assert Solution().maximumProduct(nums=[1, 2, 3, 4]) == 24
    assert Solution().maximumProduct(nums=[-1, -2, -3]) == -6


if __name__ == '__main__':
    test()
