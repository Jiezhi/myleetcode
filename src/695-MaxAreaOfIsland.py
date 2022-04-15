#!/usr/bin/env python
"""
CREATED AT: 2022/4/15
Des:
https://leetcode.com/problems/max-area-of-island/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: BFS

See: 

"""
import collections
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Runtime: 314 ms, faster than 7.48%
        Memory Usage: 14.4 MB, less than 84.37%

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 50
        grid[i][j] is either 0 or 1.
        """
        m, n = len(grid), len(grid[0])
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dq = collections.deque()
        ret = 0
        seen = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i, j) in seen:
                    continue
                seen.clear()
                dq.append((i, j))
                while dq:
                    x, y = dq.pop()
                    seen.add((x, y))
                    for dx, dy in ds:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in seen:
                            dq.append((nx, ny))
                ret = max(ret, len(seen))
        return ret


def test():
    assert Solution().maxAreaOfIsland(
        grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    ) == 6
    assert Solution().maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]) == 0


if __name__ == '__main__':
    test()
