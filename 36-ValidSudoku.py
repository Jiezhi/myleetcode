#!/usr/bin/env python
"""
CREATED AT: 2021/7/27
Des:
https://leetcode.com/problems/valid-sudoku/
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        507 / 507 test cases passed.
        Status: Accepted
        Runtime: 88 ms
        Memory Usage: 14.3 MB
        :param board:
        :return:
        """
        col_set = [[], [], [], [], [], [], [], [], []]
        sub_box = [[[], [], []], [[], [], []], [[], [], []]]
        for i in range(len(board)):
            row_set = []
            for j in range(len(board[0])):
                k = board[i][j]
                if k == '.':
                    continue
                if k in row_set or k in col_set[j] or k in sub_box[i // 3][j // 3] or int(k) < 1 or int(k) > 9:
                    return False
                row_set.append(k)
                col_set[j].append(k)
                sub_box[i // 3][j // 3].append(k)
        return True


def test():
    assert Solution().isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    )

    assert not Solution().isValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
    )

    assert not Solution().isValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         [".", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
    )


if __name__ == '__main__':
    test()
