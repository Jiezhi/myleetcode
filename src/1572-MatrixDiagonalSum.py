#!/usr/bin/env python3
"""
CREATED AT: 2022-11-12

URL: https://leetcode.com/problems/matrix-diagonal-sum/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1572-MatrixDiagonalSum

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Runtime: 222 ms, faster than 64.61%
        Memory Usage: 14.1 MB, less than 55.99%
        n == mat.length == mat[i].length
        1 <= n <= 100
        1 <= mat[i][j] <= 100
        """
        n = len(mat)
        ret = sum(mat[i][i] + mat[i][-i - 1] for i in range(n))
        return ret - mat[n // 2][n // 2] if n & 1 else ret


def test():
    assert Solution().diagonalSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
    assert Solution().diagonalSum(mat=[[5]]) == 5


if __name__ == '__main__':
    test()
