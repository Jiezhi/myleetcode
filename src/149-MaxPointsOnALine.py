#!/usr/bin/env python3
"""
CREATED AT: 2022-07-04

URL: https://leetcode.com/problems/max-points-on-a-line/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 149-MaxPointsOnALine

Difficulty: Hard

Desc: 

Tag: 

See: 

"""
import collections
import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        Runtime: 268 ms, faster than 23.04% 
        Memory Usage: 14 MB, less than 72.62% 

        1 <= points.length <= 300
        points[i].length == 2
        -10^4 <= xi, yi <= 10^4
        All the points are unique.
        """
        ret = 1
        for x1, y1 in points:
            cnt = collections.defaultdict(int)
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                elif x1 == x2:
                    cnt['h'] += 1
                    ret = max(cnt['h'] + 1, ret)
                elif y1 == y2:
                    cnt['v'] += 1
                    ret = max(cnt['v'] + 1, ret)
                else:
                    a, b = y2 - y1, x2 - x1
                    g = math.gcd(a, b)
                    k = f'{a // g}-{b // g}'
                    cnt[k] += 1
                    ret = max(cnt[k] + 1, ret)
        return ret


def test():
    assert Solution().maxPoints(points=[[1, 1], [2, 2], [3, 3]]) == 3
    assert Solution().maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4


if __name__ == '__main__':
    test()
