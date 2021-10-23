#!/usr/bin/env python
"""
CREATED AT: 2021/9/27
Des:

https://leetcode.com/problems/jump-game-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP

See: 55
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        106 / 106 test cases passed.
        Status: Accepted
        Runtime: 148 ms
        Memory Usage: 15.1 MB
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [0] * n
        last = 0
        for i in range(n):
            j = max(i + 1, last)
            while j < min(n, i + nums[i] + 1):
                dp[j] = dp[i] + 1
                j += 1
                last = j
        return dp[-1]


def test():
    assert Solution().jump(nums=[2]) == 0
    assert Solution().jump(nums=[1, 1, 1, 1, 1]) == 4
    assert Solution().jump(nums=[2, 3, 1, 1, 4]) == 2
    assert Solution().jump(nums=[2, 3, 0, 1, 4]) == 2


if __name__ == '__main__':
    test()
