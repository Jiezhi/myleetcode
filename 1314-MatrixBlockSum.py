#!/usr/bin/env python
"""
CREATED AT: 2021/10/7
Des:
https://leetcode.com/problems/matrix-block-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """
        12 / 12 test cases passed.
        Status: Accepted
        Runtime: 104 ms
        Memory Usage: 15.2 MB
        :param mat:
        :param k:
        :return:
        """
        m, n = len(mat), len(mat[0])
        ret = [[0 for _ in range(n)] for _ in range(m)]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp accumulate from [0][0] to [i][j]
        dp[0][0] = mat[0][0]
        for i in range(1, m):
            dp[i][0] = mat[i][0] + dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = mat[0][j] + dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = mat[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        for i in range(m):
            for j in range(n):
                max_r = min(i + k, m - 1)
                max_c = min(j + k, n - 1)
                ret[i][j] = dp[max_r][max_c]
                if i - k > 0:
                    ret[i][j] -= dp[i - k - 1][max_c]
                if j - k > 0:
                    ret[i][j] -= dp[max_r][j - k - 1]
                if i - k > 0 and j - k > 0:
                    ret[i][j] += dp[i - k - 1][j - k - 1]

        return ret


def test():
    assert Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1) == [[12, 21, 16], [27, 45, 33],
                                                                                     [24, 39, 28]]
    assert Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=2) == [[45, 45, 45], [45, 45, 45],
                                                                                     [45, 45, 45]]


if __name__ == '__main__':
    test()
