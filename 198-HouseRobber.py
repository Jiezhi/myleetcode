#!/usr/bin/env python
"""
CREATED AT: 2021/8/22
Des:

https://leetcode.com/problems/house-robber/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/576/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List

from tool import print_results


class Solution:
    @print_results
    def rob(self, nums: List[int]) -> int:
        """
        68 / 68 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 14.3 MB
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
        return dp[n]


def test():
    assert Solution().rob(nums=[1]) == 1
    assert Solution().rob(nums=[1, 3]) == 3
    assert Solution().rob(nums=[1, 2, 3]) == 4
    assert Solution().rob(nums=[1, 5, 3]) == 5
    assert Solution().rob(nums=[1, 2, 3, 1]) == 4
    assert Solution().rob(nums=[3, 2, 3, 8]) == 11
    assert Solution().rob(nums=[2, 7, 9, 3, 1]) == 12
    nums = [226, 174, 214, 16, 218, 48, 153, 131, 128, 17, 157, 142, 88, 43, 37, 157, 43, 221, 191, 68, 206, 23, 225,
            82, 54, 118, 111, 46, 80, 49, 245, 63, 25, 194, 72, 80, 143, 55, 209, 18, 55, 122, 65, 66, 177, 101, 63,
            201, 172, 130, 103, 225, 142, 46, 86, 185, 62, 138, 212, 192, 125, 77, 223, 188, 99, 228, 90, 25, 193, 211,
            84, 239, 119, 234, 85, 83, 123, 120, 131, 203, 219, 10, 82, 35, 120, 180, 249, 106, 37, 169, 225, 54, 103,
            55, 166, 124]
    assert Solution().rob(nums=nums) == 7102


if __name__ == '__main__':
    test()
