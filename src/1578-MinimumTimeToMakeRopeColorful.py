#!/usr/bin/env python3
"""
CREATED AT: 2022-10-03

URL: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1578-MinimumTimeToMakeRopeColorful

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Runtime: 2644 ms, faster than 28.35%
        Memory Usage: 24.7 MB, less than 86.85%

        n == colors.length == neededTime.length
        1 <= n <= 10^5
        1 <= neededTime[i] <= 10^4
        colors contains only lowercase English letters.
        """
        ret = 0
        pre, cost = '0', 0
        for c, t in zip(colors, neededTime):
            if c == pre:
                ret += min(cost, t)
                cost = max(cost, t)
            else:
                pre, cost = c, t
        return ret


def test():
    assert Solution().minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]) == 3
    assert Solution().minCost(colors="abc", neededTime=[1, 2, 3]) == 0
    assert Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]) == 2


if __name__ == '__main__':
    test()
