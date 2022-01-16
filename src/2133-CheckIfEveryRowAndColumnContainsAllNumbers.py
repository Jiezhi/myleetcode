#!/usr/bin/env python
"""
CREATED AT: 2022/1/9
Des:
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers
https://leetcode.com/contest/weekly-contest-275/problems/check-if-every-row-and-column-contains-all-numbers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        """
        n == matrix.length == matrix[i].length
        1 <= n <= 100
        1 <= matrix[i][j] <= n
        :param matrix:
        :return:
        """
        n = len(matrix)
        sample = list(range(1, n + 1))
        for i in range(n):
            if sorted(matrix[i]) != sample:
                return False
            if sorted(matrix[x][i] for x in range(n)) != sample:
                return False
        return True


def test():
    assert Solution().checkValid(matrix=[[1, 2, 3], [3, 1, 2], [2, 3, 1]])
    assert not Solution().checkValid(matrix=[[1, 1, 1], [1, 2, 3], [1, 2, 3]])
    assert not Solution().checkValid(matrix=[[1, 2, 3], [2, 1, 3], [3, 2, 1]])


if __name__ == '__main__':
    test()
