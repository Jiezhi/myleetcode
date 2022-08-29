#!/usr/bin/env python3
"""
CREATED AT: 2022-08-28

URL: https://leetcode.com/problems/sort-the-matrix-diagonally/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1329-SortTheMatrixDiagonally

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        # TODO: Use Bubble sort to save space
        Runtime: 85 ms, faster than 94.72%
        Memory Usage: 14.2 MB, less than 95.07%

        m == mat.length
        n == mat[i].length
        1 <= m, n <= 100
        1 <= mat[i][j] <= 100
        """
        m, n = len(mat), len(mat[0])
        begins = [(x, 0) for x in range(m)] + [(0, y) for y in range(1, n)]
        for i, j in begins:
            lst = []
            x, y = i, j
            while x < m and y < n:
                lst.append(mat[x][y])
                x += 1
                y += 1
            lst.sort()
            x, y = i, j
            pos = 0
            while x < m and y < n:
                mat[x][y] = lst[pos]
                x += 1
                y += 1
                pos += 1
        return mat


def test():
    assert Solution().diagonalSort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]) == [[1, 1, 1, 1], [1, 2, 2, 2],
                                                                                       [1, 2, 3, 3]]
    assert Solution().diagonalSort(
        [[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4],
         [84, 28, 14, 11, 5, 50]]) == [[5, 17, 4, 1, 52, 7], [11, 11, 25, 45, 8, 69], [14, 23, 25, 44, 58, 15],
                                       [22, 27, 31, 36, 50, 66], [84, 28, 75, 33, 55, 68]]


if __name__ == '__main__':
    test()
