#!/usr/bin/env python3
"""
CREATED AT: 2022-10-19

URL: https://leetcode.com/problems/number-of-enclaves/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1020-NumberOfEnclaves

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Runtime: 1726 ms, faster than 35.28%
        Memory Usage: 81.2 MB, less than 26.98%

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 500
        grid[i][j] is either 0 or 1.
        """
        m, n = len(grid), len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def fill(x, y):
            if not 0 <= x < m or not 0 <= y < n:
                return
            if grid[x][y] == 1:
                grid[x][y] = 0
                for dx, dy in dirs:
                    fill(x + dx, y + dy)

        for i in range(m):
            fill(i, 0)
            fill(i, n - 1)

        for i in range(n):
            fill(0, i)
            fill(m - 1, i)

        return sum(sum(grid[x]) for x in range(m))


def test():
    assert Solution().numEnclaves(grid=[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 3
    assert Solution().numEnclaves(grid=[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == 0


if __name__ == '__main__':
    test()
