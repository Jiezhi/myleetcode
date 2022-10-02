#!/usr/bin/env python3
"""
CREATED AT: 2022-10-02

URL: https://leetcode.com/problems/maximum-sum-of-an-hourglass/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 2428-MaximumSumOfAnHourglass

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        """
        m == grid.length
        n == grid[i].length
        3 <= m, n <= 150
        0 <= grid[i][j] <= 10^6
        """
        m, n = len(grid), len(grid[0])
        first_col = []
        for k in range(m - 2):
            first_col.append(
                sum(grid[i][j] for i in range(k, k + 3) for j in range(3)) - grid[k + 1][0] - grid[k + 1][2])
        ret = 0
        for i in range(m - 2):
            pre = first_col[i]
            ret = max(ret, pre)
            for j in range(1, n - 2):
                cur = pre + grid[i][j + 2] + grid[i + 2][j + 2] + grid[i + 1][j + 1] - grid[i][j - 1] - grid[i + 2][
                    j - 1] - grid[i + 1][j]
                ret = max(ret, cur)
                pre = cur
        return ret


def test():
    assert Solution().maxSum(grid=[[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]) == 30
    assert Solution().maxSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 35


if __name__ == '__main__':
    test()
