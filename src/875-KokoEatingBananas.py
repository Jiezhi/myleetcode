#!/usr/bin/env python
"""
CREATED AT: 2022/1/20
Des:

https://leetcode.com/problems/koko-eating-bananas/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

Time Spent:  min
"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Runtime: 612 ms, faster than 37.75%
        Memory Usage: 15.5 MB, less than 60.66%

        CREATED AT: 2022/1/20
        1 <= piles.length <= 10^4
        piles.length <= h <= 10^9
        1 <= piles[i] <= 10^9
        :param piles:
        :param h:
        :return:
        """
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            ret = 0
            for pile in piles:
                ret += math.ceil(pile / mid)
                if ret > h:
                    break
            if ret > h:
                low = mid + 1
            else:
                high = mid
        return low


def test():
    assert Solution().minEatingSpeed(piles=[3, 6, 7, 11], h=8) == 4
    assert Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5) == 30
    assert Solution().minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6) == 23


if __name__ == '__main__':
    test()
