#!/usr/bin/env python
"""
CREATED AT: 2022/4/2
Des:
https://leetcode.com/problems/number-of-closed-islands/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
import collections
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        Runtime: 245 ms, faster than 20.03%
        Memory Usage: 15.2 MB, less than 17.43%

        :param grid: 1 <= grid.length, grid[0].length <= 100
                     0 <= grid[i][j] <=1
        :return:
        """
        m, n = len(grid), len(grid[0])
        seen = set()
        ret = 0
        dq = collections.deque()
        # ignore the borders
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if (i, j) in seen or grid[i][j] == 1:
                    continue
                # grid[i][j] not seen and be 0
                dq.append((i, j))
                island = True
                while dq:
                    x, y = dq.popleft()
                    seen.add((x, y))
                    # if any connected point is on the border, mark this island is not closed
                    # while we need to keep track the leftover connected zero points, to add them to seen set
                    if island and (x == 0 or y == 0 or x == m - 1 or y == n - 1):
                        island = False
                    if x > 0 and (x - 1, y) not in seen and grid[x - 1][y] == 0:
                        dq.append((x - 1, y))
                    if y > 0 and (x, y - 1) not in seen and grid[x][y - 1] == 0:
                        dq.append((x, y - 1))
                    if x < m - 1 and (x + 1, y) not in seen and grid[x + 1][y] == 0:
                        dq.append((x + 1, y))
                    if y < n - 1 and (x, y + 1) not in seen and grid[x][y + 1] == 0:
                        dq.append((x, y + 1))
                ret += island
        return ret


def test():
    assert Solution().closedIsland(
        grid=[
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0]]) == 2


if __name__ == '__main__':
    test()
