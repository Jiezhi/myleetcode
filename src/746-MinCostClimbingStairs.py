#!/usr/bin/env python
"""
CREATED AT: 2021/9/25
Des:
https://leetcode.com/problems/min-cost-climbing-stairs/
GITHUB: https://github.com/Jiezhi/myleetcode
Reference: https://leetcode.com/problems/min-cost-climbing-stairs/discuss/657490/Python-solution-from-a-beginner-(some-easy-steps-to-follow-to-solve-dp)
Difficulty: Easy
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        283 / 283 test cases passed.
        Status: Accepted
        Runtime: 56 ms
        Memory Usage: 14.4 MB
        :param cost:
        :return:
        """
        if len(cost) == 1:
            return 0
        if len(cost) == 2:
            return min(cost)
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])


def test():
    assert Solution().minCostClimbingStairs(cost=[10, 15, 20]) == 15
    assert Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


if __name__ == '__main__':
    test()
