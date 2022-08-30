#!/usr/bin/env python3
"""
CREATED AT: 2022-08-30

URL: https://leetcode.com/problems/rotate-image/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/770/


GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 48-RotateImage

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        2022-08-30
        Runtime: 56 ms, faster than 49.28%
        Memory Usage: 14 MB, less than 29.99%

        Do not return anything, modify matrix in-place instead.
        n == matrix.length == matrix[i].length
        1 <= n <= 20
        -1000 <= matrix[i][j] <= 1000
        """
        n = len(matrix)

        def get_points(x, y):
            p1 = (x, y)
            p2 = (y, n - x - 1)
            p3 = (n - x - 1, n - y - 1)
            p4 = (n - y - 1, x)
            return p1, p2, p3, p4

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                (x1, y1), (x2, y2), (x3, y3), (x4, y4) = get_points(i, j)
                matrix[x2][y2], matrix[x3][y3], matrix[x4][y4], matrix[x1][y1] = \
                    matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4]

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        2021/8/2
        21 / 21 test cases passed.
        Status: Accepted
        Runtime: 64 ms
        Memory Usage: 14.3 MB
        Do not return anything, modify matrix in-place instead.
        """
        # swap four number per time,
        # and we need len(matrix) ** 2 // 4 times operation
        n = len(matrix)
        j, k = 0, 0
        level = 0
        for i in range((n ** 2 // 4), 0, -1):
            matrix[j][k], matrix[k][n - 1 - level], matrix[n - 1 - level][n - 1 - k], matrix[n - 1 - k][j] = \
                matrix[n - 1 - k][j], matrix[j][k], matrix[k][n - 1 - level], matrix[n - 1 - level][n - 1 - k]
            if k + 1 < n - 1 - level:
                k += 1
            else:
                level += 1
                j = level
                k = level


def test():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix=matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix=matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]


if __name__ == '__main__':
    test()
