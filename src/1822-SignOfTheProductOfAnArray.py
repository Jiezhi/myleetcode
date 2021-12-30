#!/usr/bin/env python
"""
CREATED AT: 2021/12/30
Des:

https://leetcode.com/problems/sign-of-the-product-of-an-array/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag:

See:

Time Spent: 1 min
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        Runtime: 60 ms, faster than 67.84%
        Memory Usage: 14.5 MB, less than 35.91%

        1 <= nums.length <= 1000
        -100 <= nums[i] <= 100
        :param nums:
        :return:
        """
        ret = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                ret *= -1
        return ret


def test():
    assert Solution().arraySign(nums=[-1, -2, -3, -4, 3, 2, 1]) == 1
    assert Solution().arraySign(nums=[1, 5, 0, 2, -3]) == 0


if __name__ == '__main__':
    test()
