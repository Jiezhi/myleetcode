#!/usr/bin/env python
"""
CREATED AT: 2021/9/21
Des:
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game
https://leetcode.com/explore/item/3981
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        100 / 100 test cases passed.
        Status: Accepted
        Runtime: 42 ms
        Memory Usage: 14.3 MB
        :param moves:
        :return:
        """
        if len(moves) < 5:
            return 'Pending'
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for x in range(0, len(moves), 2):
            matrix[moves[x][0]][moves[x][1]] = 1
        for x in range(1, len(moves), 2):
            matrix[moves[x][0]][moves[x][1]] = 2

        if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            if matrix[0][0] == 1:
                return 'A'
            elif matrix[0][0] == 2:
                return 'B'
        if matrix[0][2] == matrix[1][1] == matrix[2][0]:
            if matrix[0][2] == 1:
                return 'A'
            elif matrix[0][2] == 2:
                return 'B'
        for i in [0, 1, 2]:
            if matrix[i][0] == matrix[i][1] == matrix[i][2]:
                if matrix[i][0] == 1:
                    return 'A'
                elif matrix[i][0] == 2:
                    return 'B'
        for i in [0, 1, 2]:
            if matrix[0][i] == matrix[1][i] == matrix[2][i]:
                if matrix[0][i] == 1:
                    return 'A'
                elif matrix[0][i] == 2:
                    return 'B'
        return 'Pending' if len(moves) < 9 else 'Draw'


def test():
    assert Solution().tictactoe(moves=[[2, 0], [1, 1], [0, 2], [2, 1], [1, 2], [1, 0], [0, 0], [0, 1]]) == 'B'
    assert Solution().tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]) == 'A'
    assert Solution().tictactoe(moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]) == 'B'
    assert Solution().tictactoe(
        moves=[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]) == 'Draw'
    assert Solution().tictactoe(moves=[[0, 0], [1, 1]]) == 'Pending'


if __name__ == '__main__':
    test()
