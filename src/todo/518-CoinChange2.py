#!/usr/bin/env python
"""
CREATED AT: 2021/10/13
Des:

https://leetcode.com/problems/coin-change-2/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP

See: 322
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        1 <= coins.length <= 300
        1 <= coins[i] <= 5000
        All the values of coins are unique.
        0 <= amount <= 5000
        :param amount:
        :param coins:
        :return:
        """
        dp = [0 for _ in range(amount + 1)]
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for i in range(amount + 1):
            for c in coins:
                if i - c >= 0 and dp[i - c] > 0:
                    dp[i] += 1

        print(dp)
        return dp[-1]


def test():
    assert Solution().change(amount=5, coins=[1, 2, 5]) == 4
    assert Solution().change(amount=3, coins=[2]) == 0
    assert Solution().change(amount=10, coins=[10]) == 1


if __name__ == '__main__':
    test()
