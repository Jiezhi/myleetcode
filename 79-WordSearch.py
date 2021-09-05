#!/usr/bin/env python
"""
CREATED AT: 2021/9/5
Des:
https://leetcode.com/problems/word-search/
https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        56 / 56 test cases passed.
        Status: Accepted
        Runtime: 8288 ms
        Memory Usage: 14.2 MB
        :param board:
        :param word:
        :return:
        """
        m, n = len(board), len(board[0])
        if len(word) > m * n:
            return False

        walk_locs = []

        def forward(loc_i, loc_j) -> bool:
            if len(word) == len(walk_locs):
                return True
            x_lst = [loc_i + 1, loc_i - 1, loc_i, loc_i]
            y_lst = [loc_j, loc_j, loc_j + 1, loc_j - 1]
            for k in range(4):
                x = x_lst[k]
                y = y_lst[k]
                if 0 <= x < m and 0 <= y < n \
                        and (x, y) not in walk_locs \
                        and board[x][y] == word[len(walk_locs)]:
                    walk_locs.append((x, y))
                    if not forward(x, y):
                        walk_locs.remove((x, y))
                    else:
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[len(walk_locs)]:
                    walk_locs.append((i, j))
                    if forward(i, j):
                        return True
                    else:
                        walk_locs.remove((i, j))
        return False


def test():
    assert Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED"
    )

    assert Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE"
    )

    assert not Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB"
    )


if __name__ == '__main__':
    test()
