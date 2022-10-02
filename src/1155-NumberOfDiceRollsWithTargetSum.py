#!/usr/bin/env python3
"""
CREATED AT: 2022-10-02

URL: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1155-NumberOfDiceRollsWithTargetSum

Difficulty:  Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        Runtime: 1003 ms, faster than 38.86%
        Memory Usage: 19.8 MB, less than 26.91%

        1 <= n, k <= 30
        1 <= target <= 1000
        """
        mod = 10 ** 9 + 7

        @cache
        def dp(i, t) -> int:
            if t < i:
                return 0
            if i == 1:
                return 1 if 0 < t <= k else 0
            return sum(dp(i - 1, t - x) for x in range(1, k + 1)) % mod

        return dp(n, target)


def test():
    assert Solution().numRollsToTarget(n=1, k=6, target=3) == 1
    assert Solution().numRollsToTarget(n=2, k=6, target=7) == 6
    assert Solution().numRollsToTarget(n=30, k=30, target=500) == 222616187


if __name__ == '__main__':
    test()
