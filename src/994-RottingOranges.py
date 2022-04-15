#!/usr/bin/env python
"""
CREATED AT: 2021/10/29
Des:

https://leetcode.com/problems/rotting-oranges/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: BFS

See: 542. 01 Matrix
"""
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        AC: 04/15/2022 16:14

        Runtime: 59 ms, faster than 76.07%
        Memory Usage: 13.9 MB, less than 50.54%
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 10
        grid[i][j] is 0, 1, or 2.
        """
        m, n = len(grid), len(grid[0])
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dq = collections.deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        if not fresh:
            return 0

        seen = set()
        ret = 0
        while dq:
            x, y, k = dq.popleft()
            if (x, y) in seen or not 0 <= x < m or not 0 <= y < n:
                continue
            seen.add((x, y))
            if grid[x][y] != 0:
                if grid[x][y] == 1:
                    fresh -= 1
                ret = max(ret, k)
                for dx, dy in ds:
                    dq.append((x + dx, y + dy, k + 1))
        return -1 if fresh else ret


def test():
    assert Solution().orangesRotting(grid=[[2]]) == 0
    assert Solution().orangesRotting(grid=[[1, 2]]) == 1
    assert Solution().orangesRotting(grid=[[1, 1, 2]]) == 2
    assert Solution().orangesRotting(grid=[[2, 1, 1, 2]]) == 1
    assert Solution().orangesRotting(grid=[[2, 1, 1]]) == 2
    assert Solution().orangesRotting(grid=[[2, 0, 1]]) == -1
    assert Solution().orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert Solution().orangesRotting(grid=[[2, 1, 2], [1, 1, 1], [2, 1, 2]]) == 2
    assert Solution().orangesRotting(grid=[[2, 1, 2], [1, 0, 1], [2, 1, 2]]) == 1
    assert Solution().orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert Solution().orangesRotting(grid=[[0, 2]]) == 0


if __name__ == '__main__':
    test()
