#!/usr/bin/env python
"""
CREATED AT: 2021/10/14
Des:
https://leetcode.com/problems/unique-binary-search-trees/
https://leetcode.com/study-plan/dynamic-programming/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

TAG: DP
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Runtime: 35 ms, faster than 36.42%
        Memory Usage: 14.1 MB, less than 91.48%

        1 <= n <= 19
        :param n:
        :return:
        """
        if n <= 2:
            return n
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


def test():
    assert Solution().numTrees(n=3) == 5
    assert Solution().numTrees(n=4) == 14
    assert Solution().numTrees(n=1) == 1


if __name__ == '__main__':
    test()
