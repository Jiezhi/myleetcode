#!/usr/bin/env python
"""
CREATED AT: 2021/10/12
Des:
https://leetcode.com/problems/unique-paths-ii/
https://leetcode.com/study-plan/dynamic-programming/
https://leetcode.com/explore/featured/card/dynamic-programming/634/matrix-path-based-dp/4131/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DP
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        CREATED AT: 2021/10/12
        Runtime: 70 ms, faster than 14.61%
        Memory Usage: 14.3 MB, less than 60.08%
        :param obstacleGrid:
        :return:
        """
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 1
        found_obstacle = False
        for i in range(n):
            if found_obstacle or obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                found_obstacle = True
            else:
                dp[0][i] = 1
        found_obstacle = False
        for i in range(1, m):
            if found_obstacle or obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                found_obstacle = True
            else:
                dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


def test():
    assert Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]) == 1


if __name__ == '__main__':
    test()
