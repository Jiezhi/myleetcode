#!/usr/bin/env python
"""
CREATED AT: 2021/10/7
Des:
https://leetcode.com/problems/triangle/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        If reverse iterator triangle to avoid reverse list operation.

        44 / 44 test cases passed.
        Status: Accepted
        Runtime: 64 ms
        Memory Usage: 15.2 MB
        :param triangle:
        :return:
        """
        h = len(triangle)
        # it would be easier to sum reverse triangle
        triangle.reverse()
        dp = [triangle[0]]
        for i in range(1, h):
            tmp = []
            for j in range(h - i):
                tmp.append(triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1]))
            dp.append(tmp)
        return dp[-1][0]


def test():
    assert Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert Solution().minimumTotal(triangle=[[-10]]) == -10


if __name__ == '__main__':
    test()
