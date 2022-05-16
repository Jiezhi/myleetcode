#!/usr/bin/env python
"""
CREATED AT: 2022/5/16
Des:
https://leetcode.com/problems/shortest-path-in-binary-matrix/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Runtime: 1113 ms, faster than 20.75%
        Memory Usage: 15.4 MB, less than 26.25%
        n == grid.length
        n == grid[i].length
        1 <= n <= 100
        grid[i][j] is 0 or 1
        :param grid:
        :return:
        """
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        seen = set()
        m, n = len(grid), len(grid[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        dq = collections.deque([(0, 0, 1)])
        while dq:
            x, y, cnt = dq.popleft()
            if x == m - 1 and y == n - 1:
                return cnt
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 1 or (x, y) in seen:
                continue
            seen.add((x, y))
            for dx, dy in dirs:
                dq.append((x + dx, y + dy, cnt + 1))
        return -1


def test():
    assert Solution().shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]) == 2


if __name__ == '__main__':
    test()
