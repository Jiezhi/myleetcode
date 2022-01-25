#!/usr/bin/env python
"""
CREATED AT: 2021/10/13
Des:

https://leetcode.com/problems/coin-change-2/
https://leetcode.com/explore/featured/card/dynamic-programming/633/common-patterns-continued/4138/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP

See: 322
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Solved at 2022/01/25
        28 / 28 test cases passed.
        Status: Accepted
        Runtime: 196 ms, faster than 71.16%
        Memory Usage: 14.3 MB, less than 85.88%
        1 <= coins.length <= 300
        1 <= coins[i] <= 5000
        All the values of coins are unique.
        0 <= amount <= 5000
        :param amount:
        :param coins:
        :return:
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


def test():
    assert Solution().change(amount=5, coins=[1, 2, 5]) == 4
    assert Solution().change(amount=3, coins=[2]) == 0
    assert Solution().change(amount=10, coins=[10]) == 1


if __name__ == '__main__':
    test()
