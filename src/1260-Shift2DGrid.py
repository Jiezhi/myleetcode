#!/usr/bin/env python
"""
CREATED AT: 2022/4/11
Des:
https://leetcode.com/problems/shift-2d-grid/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        Runtime: 248 ms, faster than 47.91%
        Memory Usage: 14.5 MB, less than 13.09%

        m == grid.length
        n == grid[i].length
        1 <= m <= 50
        1 <= n <= 50
        -1000 <= grid[i][j] <= 1000
        0 <= k <= 100
        :param grid:
        :param k:
        :return:
        """
        m, n = len(grid), len(grid[0])
        lst = []
        for g in grid:
            lst += g

        k %= len(lst)

        lst = lst[-k:] + lst[:-k]

        ret = []
        for i in range(0, len(lst), n):
            ret.append(lst[i: i + n])
        return ret


def test():
    pass


if __name__ == '__main__':
    test()
