#!/usr/bin/env python
"""
CREATED AT: 2021/8/21
Des:
https://leetcode.com/problems/maximum-matrix-sum
https://leetcode.com/contest/biweekly-contest-59/problems/maximum-matrix-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        return 0


def test():
    assert Solution().maxMatrixSum(matrix=[[1, -1], [-1, 1]]) == 4
    assert Solution().maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16


if __name__ == '__main__':
    test()
