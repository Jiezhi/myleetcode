#!/usr/bin/env python
"""
CREATED AT: 2022/1/4
Des:

https://leetcode.com/problems/product-of-array-except-self/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See:

Ref:

Time Spent:  min
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        20 / 20 test cases passed.
        Status: Accepted
        Runtime: 392 ms
        Memory Usage: 21.1 MB
        2 <= nums.length <= 10^5
        -30 <= nums[i] <= 30
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = nums[i - 1] * dp[i - 1]
        acc = nums[-1]
        for i in range(n - 2, -1, -1):
            dp[i] *= acc
            acc *= nums[i]
        return dp


def test():
    assert Solution().productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
    assert Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


if __name__ == '__main__':
    test()
