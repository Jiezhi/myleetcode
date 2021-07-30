#!/usr/bin/env python
"""
CREATED AT: 2021/7/30
Des:

https://leetcode.com/problems/01-matrix/
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3831/
GITHUB: https://github.com/Jiezhi/myleetcode

"""
from typing import List


class Solution:
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
    assert Solution().updateMatrix(
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
