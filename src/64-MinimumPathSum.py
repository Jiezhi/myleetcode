#!/usr/bin/env python
"""
CREATED AT: 2021/10/9
Des:
https://leetcode.com/problems/minimum-path-sum/
https://leetcode.com/study-plan/dynamic-programming/?progress=5pg8wic
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        61 / 61 test cases passed.
        Status: Accepted
        Runtime: 100 ms
        Memory Usage: 15.6 MB
        Submitted: 0 minutes ago

        :param grid:
        :return:
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


def test():
    assert Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert Solution().minPathSum(grid=[[1, 2, 3], [4, 5, 6]]) == 12
    assert Solution().minPathSum(grid=[[1, 2, 3]]) == 6


if __name__ == '__main__':
    test()
