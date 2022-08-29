#!/usr/bin/env python3
"""
CREATED AT: 2022-08-29

URL: https://leetcode.com/problems/number-of-islands/
https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/


GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 200-NumberOfIslands

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Runtime: 375 ms, faster than 80.17%
        Memory Usage: 21.2 MB, less than 37.33%

        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'.
        """
        ret = 0
        seen = set()
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if (i, j) in seen or grid[i][j] == '0':
                    continue
                ret += 1
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if (x, y) in seen:
                        continue
                    seen.add((x, y))
                    for dx, dy in dirs:
                        if not 0 <= x + dx < m or not 0 <= y + dy < n or grid[x + dx][y + dy] == '0':
                            continue
                        stack.append((x + dx, y + dy))
        return ret

    def numIslands2(self, grid: List[List[str]]) -> int:
        """
        2019/11/22
        :param grid:
        :return:
        """
        if not grid:
            return 0
        islands = 0
        height = len(grid)
        length = len(grid[0])
        q = Queue(height * length)
        visited = set()
        for h in range(height):
            for l in range(length):
                if grid[h][l] == '1' and (h, l) not in visited:
                    q.put((h, l))
                    visited.add((h, l))
                    while not q.empty():
                        (th, tl) = q.get()
                        # Up
                        if th > 0 and grid[th - 1][tl] == '1' and (th - 1, tl) not in visited:
                            q.put((th - 1, tl))
                            visited.add((th - 1, tl))
                        # Left
                        if tl > 0 and grid[th][tl - 1] == '1' and (th, tl - 1) not in visited:
                            q.put((th, tl - 1))
                            visited.add((th, tl - 1))
                        # Down
                        if th < height - 1 and grid[th + 1][tl] == '1' and (th + 1, tl) not in visited:
                            q.put((th + 1, tl))
                            visited.add((th + 1, tl))
                        # Right
                        if tl < length - 1 and grid[th][tl + 1] == '1' and (th, tl + 1) not in visited:
                            q.put((th, tl + 1))
                            visited.add((th, tl + 1))
                    islands += 1
        return islands


def test():
    assert Solution().numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1
    assert Solution().numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3
    land = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1"],
            ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0"],
            ["1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"],
            ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
            ]
    assert Solution().numIslands(land) == 1


if __name__ == '__main__':
    test()
