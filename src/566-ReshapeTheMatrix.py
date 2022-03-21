#!/usr/bin/env python
"""
CREATED AT: 2022/3/21
Des:

https://leetcode.com/problems/reshape-the-matrix/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        Runtime: 102 ms, faster than 74.19%
        Memory Usage: 14.8 MB, less than 46.88%

        m == mat.length
        n == mat[i].length
        1 <= m, n <= 100
        -1000 <= mat[i][j] <= 1000
        1 <= r, c <= 300
        """
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        ret = []
        for i in range(m):
            ret += mat[i]

        return [ret[x * c: (x + 1) * c] for x in range(r)]


def test():
    assert Solution().matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
    assert Solution().matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]


if __name__ == '__main__':
    test()
