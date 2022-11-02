#!/usr/bin/env python3
"""
CREATED AT: 2022-11-02

URL: https://leetcode.com/problems/coordinate-with-maximum-network-quality/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1620-CoordinateWithMaximumNetworkQuality

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        """
        Runtime: 3601 ms, faster than 40.84%
        Memory Usage: 13.9 MB, less than 84.17%

        1 <= towers.length <= 50
        towers[i].length == 3
        0 <= xi, yi, qi <= 50
        1 <= radius <= 50
        """
        min_x, min_y, max_x, max_y = towers[0][0], towers[0][1], towers[0][0], towers[0][1]
        for x, y, _ in towers:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        def calc(a, b) -> int:
            r = 0
            for x, y, q in towers:
                d = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
                if d <= radius:
                    r += math.floor(q / (1 + d))
            return r

        ret = (calc(0, 0), 0, 0)
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                r = calc(x, y)
                if ret[0] < r:
                    ret = (r, x, y)
        return [ret[1], ret[2]]


def test():
    assert Solution().bestCoordinate([[44, 31, 4], [47, 27, 27], [7, 13, 0], [13, 21, 20], [50, 34, 18], [47, 44, 28]],
                                     13) == [47, 27]
    assert Solution().bestCoordinate(towers=[[1, 2, 5], [2, 1, 7], [3, 1, 9]], radius=2) == [2, 1]
    assert Solution().bestCoordinate(towers=[[23, 11, 21]], radius=9) == [23, 11]
    assert Solution().bestCoordinate(towers=[[1, 2, 13], [2, 1, 7], [0, 1, 9]], radius=2) == [1, 2]


if __name__ == '__main__':
    test()
