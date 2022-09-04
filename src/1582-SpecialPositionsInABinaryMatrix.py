#!/usr/bin/env python3
"""
CREATED AT: 2022-09-04

URL: https://leetcode.com/problems/special-positions-in-a-binary-matrix/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1582-SpecialPositionsInABinaryMatrix

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Runtime: 210 ms, faster than 76.94%
        Memory Usage: 14.3 MB, less than 58.31%
        m == mat.length
        n == mat[i].length
        1 <= m, n <= 100
        mat[i][j] is either 0 or 1.
        """
        ret = 0
        m, n = len(mat), len(mat[0])
        for i in range(m):
            if sum(mat[i]) != 1:
                continue
            for j in range(n):
                if mat[i][j] == 1:
                    if sum(mat[x][j] for x in range(m)) == 1:
                        ret += 1
                    break
        return ret


def test():
    assert Solution().numSpecial(mat=[[1, 0, 0], [0, 0, 1], [1, 0, 0]]) == 1
    assert Solution().numSpecial(mat=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3


if __name__ == '__main__':
    test()
