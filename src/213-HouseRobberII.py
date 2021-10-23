#!/usr/bin/env python
"""
CREATED AT: 2021/9/26
Des:
https://leetcode.com/problems/house-robber-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP

Also See: 198. House Robber
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        75 / 75 test cases passed.
        Status: Accepted
        Runtime: 20 ms
        Memory Usage: 14.3 MB
        :param nums:
        :return:
        """
        if len(nums) <= 3:
            return max(nums)

        def rob2(nums: List[int]) -> int:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            return dp[-1]

        # we rob twice without the first and the last separately, and choose the max one
        return max(rob2(nums[1:]), rob2(nums[:-1]))


def test():
    assert Solution().rob(nums=[4, 1, 2, 8, 1]) == 12
    assert Solution().rob(nums=[4, 1, 2, 8]) == 9
    assert Solution().rob(nums=[2, 3, 2]) == 3
    assert Solution().rob(nums=[1, 2, 3, 1]) == 4
    assert Solution().rob(nums=[1, 2, 3]) == 3


if __name__ == '__main__':
    test()
