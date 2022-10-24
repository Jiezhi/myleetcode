#!/usr/bin/env python3
"""
CREATED AT: 2022-10-24

URL: https://leetcode.com/problems/shortest-bridge/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 934-ShortestBridge

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        n == grid.length == grid[i].length
        2 <= n <= 100
        grid[i][j] is either 0 or 1.
        There are exactly two islands in grid.
        """
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y):
            connect = set()
            ret = n ** 2
            stack = [(x, y)]
            while stack:
                a, b = stack.pop()
                if not 0 <= a < n or not 0 <= b < n or (a, b) in connect or grid[a][b] == 0:
                    continue
                connect.add((a, b))
                for dx, dy in dirs:
                    stack.append((a + dx, b + dy))


            hq = [(1, x, y) for x, y in connect]
            while hq:
                d, x, y = heapq.heappop(hq)
                if not 0 <= x < n or not 0 <= y < n:
                    continue
                if grid[x][y] == 1:
                    if (x, y) not in connect:
                        ret = min(ret, d)
                if grid[x][y] == 0 or grid[x][y] >= d:
                    grid[x][y] = d
                    for dx, dy in dirs:
                        heapq.heappush(hq, (d + 1, x + dx, y + dy))
            return ret - 2


        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i, j)

def test():
    assert Solution().shortestBridge(grid = [[0,1],[1,0]]) == 1
    assert Solution().shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]) == 2
    assert Solution().shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]) == 1


if __name__ == '__main__':
    test()

