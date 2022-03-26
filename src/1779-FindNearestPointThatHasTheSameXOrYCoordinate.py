#!/usr/bin/env python
"""
CREATED AT: 2022/3/26
Des:
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/submissions/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        Runtime: 1009 ms, faster than 38.47%
        Memory Usage: 19.4 MB, less than 36.51%
        :param x:
        :param y:
        :param points:
        :return:
        """
        distance = 10 ** 5
        pos = -1
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                if abs(x - px) + abs(y - py) < distance:
                    distance = abs(x - px) + abs(y - py)
                    pos = i
        return pos


def test():
    assert Solution().nearestValidPoint(x=3, y=4, points=[[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]) == 2


if __name__ == '__main__':
    test()
