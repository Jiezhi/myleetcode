#!/usr/bin/env python
"""
CREATED AT: 2021/10/10
Des:
https://leetcode.com/problems/longest-palindromic-subsequence/
https://leetcode.com/study-plan/dynamic-programming/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP
"""
from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        AC: 05/05/2022 
        Runtime: 2385 ms, faster than 46.10%
        Memory Usage: 31.4 MB, less than 46.41%

        1 <= s.length <= 1000
        :param s:
        :return:
        """
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for left in range(n - 1, -1, -1):
            dp[left][left] = 1
            for right in range(left + 1, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])
        return dp[0][-1]

    def longestPalindromeSubseq2(self, s: str) -> int:
        """
        86 / 86 test cases passed, but took too much memory.
        """
        n = len(s)

        @lru_cache(None)
        def dp(left, right) -> int:
            if left > right:
                return 0
            if left == right:
                return 1
            ret = 0
            if s[left] == s[right]:
                ret = 2 + dp(left + 1, right - 1)
            ret = max(ret, dp(left + 1, right), dp(left, right - 1))
            return ret

        return dp(0, n - 1)


def test():
    assert Solution().longestPalindromeSubseq(s="bbbab") == 4
    assert Solution().longestPalindromeSubseq(s="cbbd") == 2


if __name__ == '__main__':
    test()
