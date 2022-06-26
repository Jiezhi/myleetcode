#!/usr/bin/env python3
"""
CREATED AT: 2022-06-26

URL: https://leetcode.com/problems/check-if-matrix-is-x-matrix/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2319-CheckIfMatrixIsX-Matrix

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        """
        n == grid.length == grid[i].length
        3 <= n <= 100
        0 <= grid[i][j] <= 10^5
        :param grid:
        :return:
        """
        seen = set()
        n = len(grid)
        for i in range(n):
            seen.add((i, i))
            seen.add((n - i - 1, i))
            if grid[i][i] == 0 or grid[n - i - 1][i] == 0:
                return False

        for i in range(n):
            for j in range(n):
                if (i, j) not in seen and grid[i][j] != 0:
                    return False
        return True


def test():
    assert Solution().checkXMatrix(grid=[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]])
    assert not Solution().checkXMatrix(grid=[[5, 7, 0], [0, 3, 1], [0, 5, 0]])


if __name__ == '__main__':
    test()
