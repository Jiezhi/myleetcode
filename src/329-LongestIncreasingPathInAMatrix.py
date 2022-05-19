#!/usr/bin/env python
"""
CREATED AT: 2022/5/19
Des:
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 1192

"""
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        Runtime: 623 ms, faster than 48.54%
        Memory Usage: 14.9 MB, less than 80.09%
        :param matrix:
        m == matrix.length
        n == matrix[i].length
        1 <= m, n <= 200
        0 <= matrix[i][j] <= 2^31 - 1
        :return:
        """
        m, n = len(matrix), len(matrix[0])
        rank = [[-1 for _ in range(n)] for _ in range(m)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ret = 0

        def dfs(x, y) -> int:
            if not (0 <= x < m and 0 <= y < n):
                return -1
            if rank[x][y] > 0:
                return rank[x][y]
            tmp_ret = 1
            for dx, dy in dirs:
                if 0 <= x + dx < m and 0 <= y + dy < n and matrix[x][y] < matrix[x + dx][y + dy]:
                    d = dfs(x + dx, y + dy)
                    tmp_ret = max(tmp_ret, d + 1)
            rank[x][y] = tmp_ret
            return tmp_ret

        for i in range(m):
            for j in range(n):
                ret = max(ret, dfs(i, j))
        return ret


def test():
    assert Solution().longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4


if __name__ == '__main__':
    test()
