#!/usr/bin/env python3
"""
CREATED AT: 2022-10-20

URL: https://leetcode.com/problems/count-sub-islands

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1905-CountSubIslands

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        Runtime: 3836 ms, faster than 84.03%
        Memory Usage: 179.4 MB, less than 5.03%
        m == grid1.length == grid2.length
        n == grid1[i].length == grid2[i].length
        1 <= m, n <= 500
        grid1[i][j] and grid2[i][j] are either 0 or 1.
        """
        m, n = len(grid1), len(grid1[0])

        seen = {}

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        tmp = set()

        def dfs(x: int, y: int) -> bool:
            if (x, y) in seen:
                return seen[(x, y)]
            if not 0 <= x < m or not 0 <= y < n or grid2[x][y] == 0 or (x, y) in tmp:
                return True
            if grid1[x][y] == 0:
                return False
            tmp.add((x, y))
            return all(dfs(x + dx, y + dy) for dx, dy in dirs)

        ret = 0

        for i in range(m):
            for j in range(n):
                if (i, j) in seen or grid2[i][j] == 0:
                    continue
                is_sub = dfs(i, j)
                if is_sub:
                    ret += 1
                for pos in tmp:
                    seen[pos] = is_sub
                tmp.clear()
        return ret


def test():
    assert Solution().countSubIslands(
        [[1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
         [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
         [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
         [1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
         [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]],
        [[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
         [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
         [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
         [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
         [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0]]) == 6
    assert Solution().countSubIslands(
        grid1=[[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
        grid2=[[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]) == 3
    assert Solution().countSubIslands(
        grid1=[[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
        grid2=[[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]) == 2


if __name__ == '__main__':
    test()
