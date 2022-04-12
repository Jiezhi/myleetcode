#!/usr/bin/env python
"""
CREATED AT: 2022/4/12
Des:
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Runtime: 199 ms, faster than 28.05%
        Memory Usage: 14.9 MB, less than 80.91%

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 100
        -100 <= grid[i][j] <= 100
        """
        return sum(1 if grid[i][j] < 0 else 0 for i in range(len(grid)) for j in range(len(grid[0])))


def test():
    assert Solution().countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
    assert Solution().countNegatives(grid=[[3, 2], [1, 0]]) == 0


if __name__ == '__main__':
    test()
