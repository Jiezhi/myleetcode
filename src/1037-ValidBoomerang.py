#!/usr/bin/env python3
"""
CREATED AT: 2022-06-08
Des: https://leetcode.com/problems/valid-boomerang/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""

from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        """
        points.length == 3
        points[i].length == 2
        0 <= xi, yi <= 100
        """
        p = sorted(points, key=lambda x: x[1])
        if p[0][1] == p[1][1] == p[2][1]:
            return False
        for i in range(2):
            if p[i][1] == p[(i + 1)][1] and p[i][0] == p[(i + 1)][0]:
                return False
        if p[1][1] - p[0][1] == 0 or p[2][1] - p[1][1] == 0:
            return True
        return not (p[1][0] - p[0][0]) * (p[2][1] - p[1][1]) == (p[2][0] - p[1][0]) * (
                p[1][1] - p[0][1])


def test():
    assert Solution().isBoomerang(points=[[1, 1], [2, 3], [3, 2]])
    assert not Solution().isBoomerang(points=[[1, 1], [2, 2], [3, 3]])
    assert not Solution().isBoomerang(points=[[1, 1], [2, 2], [2, 2]])


if __name__ == '__main__':
    test()
