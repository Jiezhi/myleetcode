#!/usr/bin/env python3
"""
CREATED AT: 2022-07-24

URL: https://leetcode.com/problems/distance-between-bus-stops/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1184-DistanceBetweenBusStops

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        """
        Runtime: 77 ms, faster than 40.68%
        Memory Usage: 15 MB, less than 47.67%

        1 <= n <= 10^4
        distance.length == n
        0 <= start, destination < n
        0 <= distance[i] <= 10^4
        """
        if start == destination:
            return 0
        if start > destination:
            return self.distanceBetweenBusStops(distance, destination, start)
        ret = sum(distance[start: destination])
        return min(sum(distance) - ret, ret)


def test():
    assert Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=1) == 1
    assert Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=2) == 3
    assert Solution().distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=3) == 4


if __name__ == '__main__':
    test()
