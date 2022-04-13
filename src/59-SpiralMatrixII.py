#!/usr/bin/env python
"""
CREATED AT: 2022/4/13
Des:
https://leetcode.com/problems/spiral-matrix-ii/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 54, 885

"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Runtime: 42 ms, faster than 63.42%
        Memory Usage: 13.8 MB, less than 85.84%

        :param n: 1 <= n <= 20
        :return:
        """
        ret = [[0 for _ in range(n)] for _ in range(n)]

        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        cur = 1
        cur_dir = 0
        while cur <= n * n:
            ret[x][y] = cur
            cur += 1
            x += dir[cur_dir][0]
            y += dir[cur_dir][1]
            if not 0 <= x < n or not 0 <= y < n or ret[x][y] > 0:
                x -= dir[cur_dir][0]
                y -= dir[cur_dir][1]
                cur_dir += 1
                cur_dir %= 4
                x += dir[cur_dir][0]
                y += dir[cur_dir][1]
        return ret


def test():
    assert Solution().generateMatrix(1) == [[1]]
    assert Solution().generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]


if __name__ == '__main__':
    test()
