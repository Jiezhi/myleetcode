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
        https://leetcode.cn/problems/shortest-bridge/solution/zui-duan-de-qiao-by-leetcode-solution-qe44/
        Runtime: 1081 ms, faster than 35.51%
        Memory Usage: 17.1 MB, less than 57.08%

        n == grid.length == grid[i].length
        2 <= n <= 100
        grid[i][j] is either 0 or 1.
        There are exactly two islands in grid.
        """
        n = len(grid)
        a_set = set()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y, s):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and (x, y) not in s:
                s.add((x, y))
                grid[x][y] = -1
                for dx, dy in dirs:
                    bfs(x + dx, y + dy, s)

        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j, a_set)
                    found = True
                    break
            if found:
                break

        q = [(x, y, 0) for x, y in a_set]
        while q:
            tmp = []
            for x, y, cnt in q:
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return cnt
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = -1
                            tmp.append((nx, ny, cnt + 1))
            q = tmp

    def shortestBridge2(self, grid: List[List[int]]) -> int:
        """
        AC on LCCN
        TLE on LC
        n == grid.length == grid[i].length
        2 <= n <= 100
        grid[i][j] is either 0 or 1.
        There are exactly two islands in grid.
        """
        n = len(grid)
        a_set = set()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y, s):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and (x, y) not in s:
                s.add((x, y))
                grid[x][y] = -1
                for dx, dy in dirs:
                    bfs(x + dx, y + dy, s)

        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j, a_set)
                    found = True
                    break
            if found:
                break

        dq = deque((x, y, 0) for x, y in a_set)
        while dq:
            x, y, cnt = dq.popleft()
            if not 0 <= x < n or not 0 <= y < n or grid[x][y] == -1:
                continue
            if grid[x][y] == 1:
                return cnt - 1
            for dx, dy in dirs:
                dq.append((x + dx, y + dy, cnt + 1))


def test():
    assert Solution().shortestBridge(grid=[[0, 1], [1, 0]]) == 1
    assert Solution().shortestBridge(grid=[[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2
    assert Solution().shortestBridge(
        grid=[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 1


if __name__ == '__main__':
    test()
