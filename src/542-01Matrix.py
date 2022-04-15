#!/usr/bin/env python
"""
CREATED AT: 2021/7/30
Des:

https://leetcode.com/problems/01-matrix/
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3831/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
import collections
from typing import List


class Solution:
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Updated at 2022/4/15
        Runtime: 869 ms, faster than 54.07%
        Memory Usage: 19.8 MB, less than 6.29%

        m == mat.length
        n == mat[i].length
        1 <= m, n <= 10^4
        1 <= m * n <= 10^4
        mat[i][j] is either 0 or 1.
        There is at least one 0 in mat.
        :param mat:
        :return:
        """
        m, n = len(mat), len(mat[0])
        MAX = m * n
        ret = [[MAX for _ in range(n)] for _ in range(m)]

        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dq = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append((i, j, 0))
        seen = set()
        while dq:
            x, y, d = dq.popleft()
            if (x, y) in seen or not 0 <= x < m or not 0 <= y < n:
                continue
            ret[x][y] = d
            seen.add((x, y))
            for dx, dy in dir:
                dq.append((x + dx, y + dy, d + 1))
        return ret

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        49 / 49 test cases passed.
        Status: Accepted
        Runtime: 564 ms
        Memory Usage: 17.2 MB
        m == mat.length
        n == mat[i].length
        1 <= m, n <= 10^4
        1 <= m * n <= 10^4
        mat[i][j] is either 0 or 1.
        There is at least one 0 in mat.
        :param mat:
        :return:
        """
        m = len(mat)
        n = len(mat[0])
        # ret = [[10001] * n] * m  This way would make disasters! `*` replicates reference for object.
        ret = [[10001 for _ in range(n)] for _ in range(m)]
        # get minimum steps from top and left
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ret[i][j] = 0
                else:
                    if i > 0:
                        ret[i][j] = min(ret[i - 1][j] + 1, ret[i][j])
                    if j > 0:
                        ret[i][j] = min(ret[i][j - 1] + 1, ret[i][j])

        # rescan to get minimum steps from bottom and right
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if ret[i][j] == 0:
                    continue
                else:
                    if i < m - 1:
                        ret[i][j] = min(ret[i + 1][j] + 1, ret[i][j])
                    if j < n - 1:
                        ret[i][j] = min(ret[i][j + 1] + 1, ret[i][j])
        return ret


def test():
    assert Solution().updateMatrix(
        mat=[[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
             [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
             [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]) == \
           [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 2, 1, 1, 0, 1], [2, 1, 1, 1, 1, 2, 1, 0, 1, 0],
            [3, 2, 2, 1, 0, 1, 0, 0, 1, 1]]
    assert Solution().updateMatrix(mat=[[0]]) == [[0]]
    assert Solution().updateMatrix(mat=[[0], [1]]) == [[0], [1]]
    assert Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    assert Solution().updateMatrix2(
        mat=[[1, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
             [0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
             [0, 1, 1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
             [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]) == \
           [[2, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 2, 2, 1], [1, 1, 1, 0, 0, 1, 2, 2, 1, 0],
            [0, 1, 2, 1, 0, 1, 2, 3, 2, 1], [0, 0, 1, 2, 1, 2, 1, 2, 1, 0], [1, 1, 2, 3, 2, 1, 0, 1, 1, 1],
            [0, 1, 2, 3, 2, 1, 1, 0, 0, 1], [1, 2, 1, 2, 1, 0, 0, 1, 1, 2], [0, 1, 0, 1, 1, 0, 1, 2, 2, 3],
            [1, 2, 1, 0, 1, 0, 1, 2, 3, 4]]


if __name__ == '__main__':
    test()
