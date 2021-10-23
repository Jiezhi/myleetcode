#!/usr/bin/env python
"""
CREATED AT: 2021/8/2
Des:

https://leetcode.com/problems/rotate-image/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/770/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
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
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    Solution().rotate(matrix=matrix)
    assert matrix == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix=matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix=matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    ans = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5]
    ]
    Solution().rotate(matrix=matrix)
    assert matrix == ans


if __name__ == '__main__':
    test()
