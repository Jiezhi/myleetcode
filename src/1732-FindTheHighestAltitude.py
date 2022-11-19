#!/usr/bin/env python3
"""
CREATED AT: 2022-11-19

URL: https://leetcode.com/problems/find-the-highest-altitude/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1732-FindTheHighestAltitude

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Runtime: 77 ms, faster than 18.16%
        Memory Usage: 13.9 MB, less than 9.99%
        n == gain.length
        1 <= n <= 100
        -100 <= gain[i] <= 100
        """
        return max(itertools.accumulate(gain, initial=0))


def test():
    assert Solution().largestAltitude(gain=[-5, 1, 5, 0, -7]) == 1
    assert Solution().largestAltitude(gain=[-4, -3, -2, -1, 4, 3, 2]) == 0


if __name__ == '__main__':
    test()
