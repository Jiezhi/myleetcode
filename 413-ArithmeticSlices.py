#!/usr/bin/env python
"""
CREATED AT: 2021/10/13
Des:
https://leetcode.com/problems/arithmetic-slices/
https://leetcode.com/study-plan/dynamic-programming
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DP

See:
"""
from functools import lru_cache
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Runtime: 56 ms, faster than 25.78%
        Memory Usage: 14.3 MB, less than 90.74%

        1 <= nums.length <= 5000
        -1000 <= nums[i] <= 1000
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return 0

        @lru_cache(None)
        def dp(n):
            """
            dp[i] = dp[i - 1] + i - 1 if i >0
            dp[i] = 0 if i == 0
            :param n:
            :return:
            """
            if n <= 2:
                return 0
            last = 0
            for i in range(1, n):
                cur = last + i - 1
                last = cur
            return last

        sub = []
        for i in range(1, len(nums)):
            sub.append(nums[i] - nums[i - 1])

        ret = 0
        cnt = 2
        cur = sub[0]
        i = 1
        while i < len(sub):
            if sub[i] == cur:
                cnt += 1
            else:
                cur = sub[i]
                ret += dp(cnt)
                cnt = 2
            i += 1
        ret += dp(cnt)
        return ret


def test():
    assert Solution().numberOfArithmeticSlices(nums=[1, 2, 3]) == 1
    assert Solution().numberOfArithmeticSlices(nums=[1, 2, 3, 4]) == 3
    assert Solution().numberOfArithmeticSlices(nums=[1]) == 0


if __name__ == '__main__':
    test()
