#!/usr/bin/env python3
"""
CREATED AT: 2022-10-31

URL: https://leetcode.com/problems/toeplitz-matrix/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 766-ToeplitzMatrix

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Runtime: 220 ms, faster than 18.00%
        Memory Usage: 14 MB, less than 36.74%

        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 20
        0 <= matrix[i][j] <= 99
        """
        m, n = len(matrix), len(matrix[0])

        def check(x, y) -> bool:
            while x < m - 1 and y < n - 1:
                x += 1
                y += 1
                if matrix[x][y] != matrix[x - 1][y - 1]:
                    return False
            return True

        for i in range(m):
            if not check(i, 0):
                return False
        for i in range(1, n):
            if not check(0, i):
                return False
        return True


def test():
    assert Solution().isToeplitzMatrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
    assert not Solution().isToeplitzMatrix(matrix=[[1, 2], [2, 2]])


if __name__ == '__main__':
    test()
