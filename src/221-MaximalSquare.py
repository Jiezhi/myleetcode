#!/usr/bin/env python
"""
CREATED AT: 2021/10/10
Des:
https://leetcode.com/problems/maximal-square/
https://leetcode.com/study-plan/dynamic-programming/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tags: DP
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        Runtime: 1936 ms, faster than 5.03%
        Memory Usage: 15.5 MB, less than 75.88%
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 300
        matrix[i][j] is '0' or '1'.
        :param matrix:
        :return:
        """
        m, n = len(matrix), len(matrix[0])
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    k = 1
                    ex = False
                    while not ex:
                        for r in range(k):
                            if j + k >= n or i + r >= m or matrix[i + r][j + k] == '0':
                                ex = True
                                break
                            if j + r >= n or i + k >= m or matrix[i + k][j + r] == '0':
                                ex = True
                                break
                            if matrix[i + k][j + k] == '0':
                                ex = True
                                break
                        k += 1
                    ret = max(ret, (k - 1) ** 2)

        return ret


def test():
    assert Solution().maximalSquare(
        matrix=[["0", "1", "1", "0", "0", "1", "0", "1", "0", "1"],
                ["0", "0", "1", "0", "1", "0", "1", "0", "1", "0"],
                ["1", "0", "0", "0", "0", "1", "0", "1", "1", "0"],
                ["0", "1", "1", "1", "1", "1", "1", "0", "1", "0"],
                ["0", "0", "1", "1", "1", "1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0", "1", "1", "1", "1", "0"],
                ["0", "0", "0", "1", "1", "0", "0", "0", "1", "0"],
                ["1", "1", "0", "1", "1", "0", "0", "1", "1", "1"],
                ["0", "1", "0", "1", "1", "0", "1", "0", "1", "1"]]) == 4

    assert Solution().maximalSquare(matrix=[["0", "1"], ["1", "0"]]) == 1
    assert Solution().maximalSquare(matrix=[["1", "1"], ["1", "1"]]) == 4
    assert Solution().maximalSquare(matrix=[["0"]]) == 0


if __name__ == '__main__':
    test()
