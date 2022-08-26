#!/usr/bin/env python3
"""
CREATED AT: 2022-08-26

URL: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1464-MaximumProductOfTwoElementsInAnArray

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Runtime: 90 ms, faster than 44.43%
        Memory Usage: 13.9 MB, less than 86.51%
        2 <= nums.length <= 500
        1 <= nums[i] <= 10^3
        """
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


def test():
    assert Solution().maxProduct(nums=[3, 4, 5, 2]) == 12
    assert Solution().maxProduct(nums=[1, 5, 4, 5]) == 16
    assert Solution().maxProduct(nums=[3, 7]) == 12


if __name__ == '__main__':
    test()
