#!/usr/bin/env python
"""
CREATED AT: 2021/9/13
Solved at: 2021/10/13
Des:

https://leetcode.com/problems/coin-change
https://leetcode.com/study-plan/dynamic-programming/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/111/dynamic-programming/809/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

TAG: DP
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Thought this as climbing stairs

        188 / 188 test cases passed.
        Status: Accepted
        Runtime: 2072 ms
        Memory Usage: 14.5 MB
        1 <= coins.length <= 12
        1 <= coins[i] <= 2^31 - 1
        0 <= amount <= 10^4
        :param coins:
        :param amount:
        :return:
        """
        # the change count must smaller than the amount value
        dp = [amount + 1 for _ in range(amount + 1)]
        # we stand at the first position and start from 0
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1


def test():
    assert Solution().coinChange([411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864) == 24
    assert Solution().coinChange(coins=[186, 419, 83, 408], amount=6249) == 20
    assert Solution().coinChange(coins=[1, 2, 5], amount=100) == 20
    assert Solution().coinChange(coins=[1, 2, 5], amount=101) == 21
    assert Solution().coinChange(coins=[1, 2, 5], amount=101) == 21
    assert Solution().coinChange(coins=[1, 2, 5], amount=11) == 3
    assert Solution().coinChange(coins=[2], amount=3) == -1
    assert Solution().coinChange(coins=[1], amount=0) == 0
    assert Solution().coinChange(coins=[1], amount=1) == 1
    assert Solution().coinChange(coins=[1], amount=2) == 2


if __name__ == '__main__':
    test()
