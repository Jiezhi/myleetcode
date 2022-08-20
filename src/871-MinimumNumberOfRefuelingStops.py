#!/usr/bin/env python3
"""
CREATED AT: 2022-08-20

URL: https://leetcode.com/problems/minimum-number-of-refueling-stops/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 871-MinimumNumberOfRefuelingStops

Difficulty: Hard

Desc:

Tag:

See:

"""
from tool import *


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Runtime: 143 ms, faster than 86.05%
        Memory Usage: 14.3 MB, less than 36.38%

        1 <= target, startFuel <= 10^9
        0 <= stations.length <= 500
        0 <= positioni <= positioni+1 < target
        1 <= fueli < 10^9
        """
        cur, ret = startFuel, 0
        hq = []
        stations.append([target, 0])
        for pos, fuel in stations:
            while hq and cur < pos:
                cur -= heapq.heappop(hq)
                ret += 1
            if cur < pos:
                return -1
            heapq.heappush(hq, -fuel)
        return ret

    def minRefuelStops2(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        LTE
        1 <= target, startFuel <= 10^9
        0 <= stations.length <= 500
        0 <= positioni <= positioni+1 < target
        1 <= fueli < 10^9
        """
        n = len(stations)

        @cache
        def dp(pos, fuel) -> int:
            if fuel >= target:
                return 0
            if pos >= n or fuel < stations[pos][0]:
                return n + 1
            return min(dp(pos + 1, fuel), dp(pos + 1, fuel + stations[pos][1]) + 1)

        ret = dp(0, startFuel)
        return ret if ret < n + 1 else -1


def test():
    assert Solution().minRefuelStops(target=1, startFuel=1, stations=[]) == 0
    assert Solution().minRefuelStops(target=100, startFuel=1, stations=[[10, 100]]) == -1
    assert Solution().minRefuelStops(target=100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]]) == 2


if __name__ == '__main__':
    test()
