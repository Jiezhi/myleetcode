#!/usr/bin/env python
"""
CREATED AT: 2022/4/26
Des:

https://leetcode.com/problems/projection-area-of-3d-shapes/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        """
        Runtime: 115 ms, faster than 38.19%
        Memory Usage: 14 MB, less than 62.85%

        n == grid.length == grid[i].length
        1 <= n <= 50
        0 <= grid[i][j] <= 50
        """
        n = len(grid)
        return n * n + sum(max(x) for x in grid) + sum(max(grid[i][j] for i in range(n)) for j in range(n)) - sum(
            1 if grid[i][j] == 0 else 0 for i in range(n) for j in range(n))


def test():
    assert Solution().projectionArea(grid=[[1, 2], [3, 4]]) == 17


if __name__ == '__main__':
    test()
