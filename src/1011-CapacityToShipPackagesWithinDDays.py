#!/usr/bin/env python3
"""
CREATED AT: 2023-03-06

URL: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1011-CapacityToShipPackagesWithinDDays

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(cap: int) -> bool:
            took_day, took_cap = 1, 0
            for weight in weights:
                if took_cap + weight > cap:
                    took_day += 1
                    took_cap = weight
                    if took_day > days:
                        return False
                else:
                    took_cap += weight

            return took_day <= days

        low, high = max(weights), sum(weights) + 1
        while low < high:
            mid = (high + low) // 2
            if canship(mid):
                high = mid
            else:
                low = mid + 1
        return low


def test():
    assert Solution().shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5) == 15


if __name__ == '__main__':
    test()

