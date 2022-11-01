#!/usr/bin/env python3
"""
CREATED AT: 2022-11-01

URL: https://leetcode.com/problems/where-will-the-ball-fall/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1706-WhereWillTheBallFall

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """
        Runtime: 246 ms, faster than 82.02%
        Memory Usage: 14.6 MB, less than 12.94%
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 100
        grid[i][j] is 1 or -1.
        """
        m, n = len(grid), len(grid[0])
        ret = []

        def fall(x, y) -> int:
            if x == m and 0 <= y < n:
                return y
            if not 0 <= x < m or not 0 <= y < n:
                return -1
            if grid[x][y] == -1:
                if y == 0 or grid[x][y - 1] == 1:
                    return -1
                return fall(x + 1, y - 1)
            else:
                if y == n - 1 or grid[x][y + 1] == -1:
                    return -1
                return fall(x + 1, y + 1)

        for i in range(n):
            ret.append(fall(0, i))
        return ret


def test():
    assert Solution().findBall(
        grid=[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]) == [1,
                                                                                                                     -1,
                                                                                                                     -1,
                                                                                                                     -1,
                                                                                                                     -1]
    assert Solution().findBall(grid=[[-1]]) == [-1]


if __name__ == '__main__':
    test()
