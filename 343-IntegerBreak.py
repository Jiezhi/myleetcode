#!/usr/bin/env python
"""
CREATED AT: 2021/10/14
Des:

https://leetcode.com/problems/integer-break/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DP

See: 
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        Runtime: 54 ms, faster than 16.59%
        Memory Usage: 14.2 MB, less than 48.49%
        2 <= n <= 58
        :param n:
        :return:
        """
        if n <= 3:
            return n - 1
        dp = [0 for _ in range(n + 1)]
        dp[2] = 2  # n = 2
        dp[3] = 3  # n = 3
        for i in range(4, n + 1):
            # skip j = 1
            dp[i] = max([dp[j] * dp[i - j] for j in range(2, i // 2 + 1)])
        return dp[-1]


def test():
    assert Solution().integerBreak(n=2) == 1
    assert Solution().integerBreak(n=3) == 2
    assert Solution().integerBreak(n=10) == 36
    assert Solution().integerBreak(n=58) == 1549681956


if __name__ == '__main__':
    test()
