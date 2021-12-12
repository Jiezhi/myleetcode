#!/usr/bin/env python
"""
CREATED AT: 2021/12/12
Des:
https://leetcode.com/problems/rings-and-rods
https://leetcode.com/contest/weekly-contest-271/problems/rings-and-rods/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent: 4 min
"""


class Solution:
    def countPoints(self, rings: str) -> int:
        """
        rings.length == 2 * n
        1 <= n <= 100
        rings[i] where i is even is either 'R', 'G', or 'B' (0-indexed).
        rings[i] where i is odd is a digit from '0' to '9' (0-indexed).
        :param rings:
        :return:
        """
        rods = [dict() for _ in range(10)]
        for i in range(0, len(rings), 2):
            rods[int(rings[i + 1])][rings[i]] = 1
        ret = 0
        for i in range(10):
            if len(rods[i]) == 3:
                ret += 1
        return ret


def test():
    assert Solution().countPoints(rings="B0B6G0R6R0R6G9") == 1
    assert Solution().countPoints(rings="B0R0G0R9R0B0G0") == 1
    assert Solution().countPoints(rings="G4") == 0


if __name__ == '__main__':
    test()
