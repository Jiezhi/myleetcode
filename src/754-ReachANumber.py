#!/usr/bin/env python3
"""
CREATED AT: 2022-11-04

URL: https://leetcode.com/problems/reach-a-number/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 754-ReachANumber

Difficulty: Medium

Desc: 

Tag: 

See:  https://leetcode.com/problems/reach-a-number/solution/

"""


class Solution:
    def reachNumber(self, target: int) -> int:
        """
        Runtime: 178 ms, faster than 52.74%
        Memory Usage: 13.8 MB, less than 60.62%
        -10^9 <= target <= 10^9
        target != 0
        """
        target = abs(target)
        ret = 0
        while target > 0:
            ret += 1
            target -= ret
        if target & 1:
            return ret + 1 + ret % 2
        else:
            return ret


def test():
    assert Solution().reachNumber(target=2) == 3
    assert Solution().reachNumber(target=3) == 2


if __name__ == '__main__':
    test()
