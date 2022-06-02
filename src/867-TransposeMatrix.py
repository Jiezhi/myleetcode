#!/usr/bin/env python
"""
CREATED AT: 2022-06-02
Des: https://leetcode.com/problems/transpose-matrix/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 77 ms, faster than 84.25%
        Memory Usage: 14.8 MB, less than 16.92%
        :param matrix:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 1000
        1 <= m * n <= 10^5
        -10^9 <= matrix[i][j] <= 10^9
        :return:
        """
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def test():
    assert Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


if __name__ == '__main__':
    test()
