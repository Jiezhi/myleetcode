#!/usr/bin/env python
"""
CREATED AT: 2021/9/26
Des:
https://leetcode.com/problems/delete-and-earn/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP

Reference: 198
"""
from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        48 / 48 test cases passed.
        Status: Accepted
        Runtime: 52 ms
        Memory Usage: 14.8 MB

        Details See Leetcode 198
        :param nums:
        :return:
        """
        cnts = Counter(nums)
        # fill the gap with 0
        nums = [cnts.get(i, 0) * i for i in range(min(cnts.keys()), max(cnts.keys()) + 1)]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


def test():
    assert Solution().deleteAndEarn(nums=[3, 4, 2]) == 6
    assert Solution().deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]) == 9


if __name__ == '__main__':
    test()
