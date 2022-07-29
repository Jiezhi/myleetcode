#!/usr/bin/env python3
"""
CREATED AT: 2022-07-29

URL: https://leetcode.com/problems/valid-square/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 593-ValidSquare

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        Runtime: 49 ms, faster than 60.65%
        Memory Usage: 13.9 MB, less than 49.77%

        p1.length == p2.length == p3.length == p4.length == 2
        -10^4 <= xi, yi <= 10^4
        """
        if len({tuple(p1), tuple(p2), tuple(p3), tuple(p4)}) != 4:
            return False

        def dist(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        l = sorted([dist(p1, p2), dist(p3, p2), dist(p1, p3)])
        if l[0] != l[1] or l[0] + l[1] != l[2]:
            return False

        b = l[0]

        l = sorted([dist(p2, p3), dist(p3, p4), dist(p2, p4)])
        if l[0] != l[1] or l[0] + l[1] != l[2] or l[0] != b:
            return False

        return True


def test():
    assert Solution().validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 1])
    assert not Solution().validSquare(p1=[0, 0], p2=[0, 0], p3=[0, 0], p4=[0, 0])
    assert not Solution().validSquare(p1=[0, 0], p2=[1, 1], p3=[1, 0], p4=[0, 12])
    assert Solution().validSquare(p1=[1, 0], p2=[-1, 0], p3=[0, 1], p4=[0, -1])


if __name__ == '__main__':
    test()
