#!/usr/bin/env python3
"""
CREATED AT: 2022-11-17

URL: https://leetcode.com/problems/rectangle-area/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 223-RectangleArea

Difficulty: Medium

Desc: 

Tag: 

See: https://leetcode.com/problems/rectangle-area/solution/

"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
        Runtime: 118 ms, faster than 32.31%
        Memory Usage: 14 MB, less than 71.27%

        -10^4 <= ax1 <= ax2 <= 10^4
        -10^4 <= ay1 <= ay2 <= 10^4
        -10^4 <= bx1 <= bx2 <= 10^4
        -10^4 <= by1 <= by2 <= 10^4
        """

        def crossedArea() -> int:
            dx = min(ax2, bx2) - max(ax1, bx1)
            dy = min(ay2, by2) - max(ay1, by1)
            return dx * dy if dx > 0 and dy > 0 else 0

        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - crossedArea()


def test():
    assert Solution().computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2) == 45
    assert Solution().computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2) == 16


if __name__ == '__main__':
    test()
