#!/usr/bin/env python3
"""
CREATED AT: 2022-10-20

URL: https://leetcode.com/problems/as-far-from-land-as-possible/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1162-AsFarFromLandAsPossible

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        Runtime: 1551 ms, faster than 36.89%
        Memory Usage: 14.7 MB, less than 67.90%

        n == grid.length
        n == grid[i].length
        1 <= n <= 100
        grid[i][j] is 0 or 1
        """
        n = len(grid)
        max_flag = n * n
        ret = [[max_flag for _ in range(n)] for _ in range(n)]

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def fill(x, y, num):
            hq = [(num, x, y)]
            while hq:
                num, x, y = heapq.heappop(hq)
                if not 0 <= x < n or not 0 <= y < n or ret[x][y] <= num:
                    continue
                if grid[x][y] == 1:
                    ret[x][y] = 0
                else:
                    ret[x][y] = num
                for dx, dy in dirs:
                    heapq.heappush(hq, (ret[x][y] + 1, x + dx, y + dy))

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and ret[i][j] != 0:
                    fill(i, j, 0)

        max_ret = max(max(x) for x in ret)
        return -1 if max_ret == 0 or max_ret == max_flag else max_ret


def test():
    assert Solution().maxDistance(grid=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert Solution().maxDistance(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4


if __name__ == '__main__':
    test()
