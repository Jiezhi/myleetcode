#!/usr/bin/env python
"""
CREATED AT: 2021/10/12
Des:
https://leetcode.com/problems/minimum-falling-path-sum/
https://leetcode.com/study-plan/dynamic-programming
https://leetcode.com/explore/featured/card/dynamic-programming/634/matrix-path-based-dp/4133/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: DP

See: 120
"""
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        CREATED AT: 2021/10/12
        Runtime: 116 ms, faster than 76.52%
        Memory Usage: 15.2 MB, less than 38.08%
        n == matrix.length
        n == matrix[i].length
        1 <= n <= 100
        -100 <= matrix[i][j] <= 100
        :param matrix:
        :return:
        """
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        # only two line dp[] needed, while this would be ok.
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == n - 1:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
        return min(dp[-1])


def test():
    assert Solution().minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert Solution().minFallingPathSum(matrix=[[-19, 57], [-40, -5]]) == -59
    assert Solution().minFallingPathSum(matrix=[[-48]]) == -48


if __name__ == '__main__':
    test()
