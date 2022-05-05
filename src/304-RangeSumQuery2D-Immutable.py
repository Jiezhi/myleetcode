#!/usr/bin/env python
"""
CREATED AT: 2022/5/5
Des:
https://leetcode.com/problems/range-sum-query-2d-immutable/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class NumMatrix:
    """
    Runtime: 1525 ms, faster than 89.14%
    Memory Usage: 25.1 MB, less than 28.71%

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -10^5 <= matrix[i][j] <= 10^5
    0 <= row1 <= row2 < m
    0 <= col1 <= col2 < n
    At most 10^4 calls will be made to sumRegion.
    """

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.acc = [[0 for _ in range(n)] for _ in range(m)]
        self.acc[0][0] = matrix[0][0]
        for i in range(1, m):
            self.acc[i][0] = matrix[i][0] + self.acc[i - 1][0]
        for j in range(1, n):
            self.acc[0][j] = matrix[0][j] + self.acc[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                self.acc[i][j] = matrix[i][j] + self.acc[i - 1][j] + self.acc[i][j - 1] - self.acc[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret = self.acc[row2][col2]
        if row1 > 0 and col1 > 0:
            ret += self.acc[row1 - 1][col1 - 1] - self.acc[row1 - 1][col2] - self.acc[row2][col1 - 1]
        elif row1 > 0:
            ret -= self.acc[row1 - 1][col2]
        elif col1 > 0:
            ret -= self.acc[row2][col1 - 1]
        return ret


def test():
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(2, 1, 4, 3) == 8
    assert obj.sumRegion(1, 1, 2, 2) == 11
    assert obj.sumRegion(1, 2, 2, 4) == 12


if __name__ == '__main__':
    test()
