#!/usr/bin/env python3
"""
CREATED AT: 2022-10-19

URL: https://leetcode.com/problems/surrounded-regions/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 130-SurroundedRegions

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Runtime: 400 ms, faster than 19.80%
        Memory Usage: 15.9 MB, less than 53.88%
        Do not return anything, modify board in-place instead.
        m == board.length
        n == board[i].length
        1 <= m, n <= 200
        board[i][j] is 'X' or 'O'.
        """
        m, n = len(board), len(board[0])
        oset = set()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n:
                return
            if (x, y) in oset or board[x][y] == 'X':
                return
            oset.add((x, y))
            for dx, dy in dirs:
                dfs(x + dx, y + dy)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O' and (i, j) not in oset:
                    board[i][j] = 'X'


def test():
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    Solution().solve(board)
    assert board == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
    board = [["X"]]
    Solution().solve(board)
    assert board == [["X"]]


if __name__ == '__main__':
    test()
