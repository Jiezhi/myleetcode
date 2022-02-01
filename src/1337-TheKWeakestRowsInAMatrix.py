#!/usr/bin/env python
"""
CREATED AT: 2022/2/1
Des:

https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
https://leetcode.com/explore/featured/card/heap/646/practices/4085/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Runtime: 134 ms, faster than 46.73%
        Memory Usage: 14.2 MB, less than 99.20%
        m == mat.length
        n == mat[i].length
        2 <= n, m <= 100
        1 <= k <= m
        matrix[i][j] is either 0 or 1.
        :param mat:
        :param k:
        :return:
        """
        m, n = len(mat), len(mat[0])
        ret = []
        for i in range(m):
            row_len = 0
            j = 0
            while j < n and mat[i][j] == 1:
                row_len += 1
                j += 1
            ret.append((row_len, i))
        ret = sorted(ret)
        return [x[1] for x in ret[:k]]


def test():
    assert Solution().kWeakestRows(
        mat=[[1, 1, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1]],
        k=3) == [2, 0, 3]

    assert Solution().kWeakestRows(
        mat=[[1, 0, 0, 0],
             [1, 1, 1, 1],
             [1, 0, 0, 0],
             [1, 0, 0, 0]],
        k=2) == [0, 2]


if __name__ == '__main__':
    test()
