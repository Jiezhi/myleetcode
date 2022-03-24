#!/usr/bin/env python
"""
CREATED AT: 2022/3/24
Des:

https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Runtime: 40 ms, faster than 57.92%
        Memory Usage: 13.9 MB, less than 63.49%

        0 <= low <= high <= 10^9
        """
        return ((high + 1) >> 1) - (low >> 1)


def test():
    assert Solution().countOdds(low=3, high=7) == 3
    assert Solution().countOdds(low=8, high=10) == 1


if __name__ == '__main__':
    test()
