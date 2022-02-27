#!/usr/bin/env python
"""
CREATED AT: 2022/2/27
Des:

https://leetcode.com/problems/minimum-time-to-complete-trips/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """
        Runtime: 2268 ms, faster than 90.00%
        Memory Usage: 28.6 MB, less than 60.00%

        1 <= time.length <= 10^5
        1 <= time[i], totalTrips <= 10^7

        :param time:
        :param totalTrips:
        :return:
        """
        lo, hi = 1, min(time) * totalTrips
        mid = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            trips = sum(mid // x for x in time)
            if trips == totalTrips:
                break
            elif trips > totalTrips:
                hi = mid - 1
            else:
                lo = mid + 1
        ret = mid
        if sum(ret // x for x in time) < totalTrips:
            ret += 1
            while sum(ret // x for x in time) < totalTrips:
                ret += 1
            return ret
        else:
            ret -= 1
            while sum(ret // x for x in time) >= totalTrips:
                ret -= 1
            return ret + 1


def test():
    assert Solution().minimumTime(time=[1, 2, 3], totalTrips=5) == 3
    assert Solution().minimumTime(time=[2], totalTrips=1) == 2


if __name__ == '__main__':
    test()
