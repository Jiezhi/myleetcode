#!/usr/bin/env python
"""
CREATED AT: 2021/8/26
Des:
https://leetcode.com/problems/set-matrix-zeroes/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        164 / 164 test cases passed.
        Status: Accepted
        Runtime: 269 ms
        Memory Usage: 15.3 MB
        Do not return anything, modify matrix in-place instead.
        """
        # record the first zero row and column position to save other zeros positions.
        r, c = None, None
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # meet first zero, and r, c used to save left zero positions
                    if r is None:
                        r, c = i, j
                    else:
                        matrix[r][j] = 0
                        matrix[i][c] = 0
        if r is None:
            return
        for i in range(m):
            if i == r:
                continue
            if matrix[i][c] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(n):
            if j == c:
                continue
            if matrix[r][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        for i in range(m):
            matrix[i][c] = 0
        for j in range(n):
            matrix[r][j] = 0


def test():
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    matrix = [[1, 3, 6, 7, 8, 9], [5, 4, 3, 2, 7, 0], [0, 3, 8, 10, 15, 7], [0, 1, 1, 5, 8, 6]]
    Solution().setZeroes(matrix)
    assert matrix == [[0, 3, 6, 7, 8, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


if __name__ == '__main__':
    test()
