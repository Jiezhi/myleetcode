#!/usr/bin/env python
"""
CREATED AT: 2022/4/12
Des:

https://leetcode.com/problems/game-of-life/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Runtime: 44 ms, faster than 60.61%
        Memory Usage: 14 MB, less than 51.25%

        m == board.length
        n == board[i].length
        1 <= m, n <= 25
        board[i][j] is 0 or 1.

        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def get_live_nb(x: int, y: int) -> int:
            cnt = 0
            if x > 0:
                if y > 0:
                    cnt += abs(board[x - 1][y - 1]) == 1
                if y < n - 1:
                    cnt += abs(board[x - 1][y + 1]) == 1
                cnt += abs(board[x - 1][y]) == 1
            if y > 0:
                cnt += abs(board[x][y - 1]) == 1
            if y < n - 1:
                cnt += abs(board[x][y + 1]) == 1

            if x < m - 1:
                if y > 0:
                    cnt += abs(board[x + 1][y - 1]) == 1
                if y < n - 1:
                    cnt += abs(board[x + 1][y + 1]) == 1
                cnt += abs(board[x + 1][y]) == 1
            return cnt

        for i in range(m):
            for j in range(n):
                nb = get_live_nb(i, j)
                if board[i][j] == 0 and nb == 3:
                    board[i][j] = 2
                elif board[i][j] == 1:
                    if nb < 2 or nb > 3:
                        board[i][j] = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0


def test():
    pass


if __name__ == '__main__':
    test()
