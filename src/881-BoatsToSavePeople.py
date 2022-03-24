#!/usr/bin/env python
"""
CREATED AT: 2022/3/24
Des:
https://leetcode.com/problems/boats-to-save-people/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 

"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Runtime: 592 ms, faster than 54.25%
        Memory Usage: 20.9 MB, less than 34.38%

        1 <= people.length <= 5 * 10^4
        1 <= people[i] <= limit <= 3 * 10^4
        """
        people = sorted(people)
        ret = 0
        lo, hi = 0, len(people) - 1
        while lo <= hi:
            if people[hi] == limit or people[hi] + people[lo] > limit:
                ret += 1
                hi -= 1
            else:
                ret += 1
                hi -= 1
                lo += 1
        return ret


def test():
    assert Solution().numRescueBoats([3, 2, 2, 1], 3) == 3
    assert Solution().numRescueBoats([3, 5, 3, 4], 5) == 4


if __name__ == '__main__':
    test()
