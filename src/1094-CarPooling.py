#!/usr/bin/env python
"""
CREATED AT: 2022/1/6
Des:

https://leetcode.com/problems/car-pooling/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent: 35 min
"""
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Runtime: 148 ms, faster than 10.14%
        Memory Usage: 14.8 MB, less than 77.09%
        1 <= trips.length <= 1000
        trips[i].length == 3
        1 <= numPassengersi <= 100
        0 <= fromi < toi <= 1000
        1 <= capacity <= 10^5
        :param trips:
        :param capacity:
        :return:
        """
        trips = sorted(trips, key=lambda trip: trip[1])
        curr_cap = 0
        dq = []
        curr_pos = 0
        for trip in trips:
            if trip[1] > curr_pos:
                curr_pos = trip[1]
            # down first,  up later
            # 先下后上，文明乘车
            while len(dq) > 0 and dq[0][2] <= curr_pos:
                curr_cap -= dq[0][0]
                dq.pop(0)
            # sort by leave position
            i = 0
            while i < len(dq):
                if trip[2] > dq[i][2]:
                    i += 1
                else:
                    break
            dq.insert(i, trip)
            curr_cap += trip[0]
            if curr_cap > capacity:
                return False
        return True


def test():
    assert Solution().carPooling([[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]], capacity=23)
    assert not Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4)
    assert Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5)
    assert Solution().carPooling(trips=[[5, 1, 5], [5, 5, 7]], capacity=5)


if __name__ == '__main__':
    test()
