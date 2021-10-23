#!/usr/bin/env python
"""
CREATED AT: 2021/10/4
Des:
https://leetcode.com/problems/island-perimeter

GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        5833 / 5833 test cases passed.
        Status: Accepted
        Runtime: 842 ms
        Memory Usage: 14.4 MB
        :param grid:
        :return:
        """
        ret = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:
                        ret += 1
                    if i == m - 1 or grid[i + 1][j] == 0:
                        ret += 1
                    if j == 0 or grid[i][j - 1] == 0:
                        ret += 1
                    if j == n - 1 or grid[i][j + 1] == 0:
                        ret += 1
        return ret


def test():
    assert Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    assert Solution().islandPerimeter(grid=[[1]]) == 4
    assert Solution().islandPerimeter(grid=[[1, 0]]) == 4
    assert Solution().islandPerimeter(grid=[[1, 1], [1, 1]]) == 8


if __name__ == '__main__':
    test()
