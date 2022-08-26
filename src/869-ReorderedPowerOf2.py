#!/usr/bin/env python3
"""
CREATED AT: 2022-08-26

URL: https://leetcode.com/problems/reordered-power-of-2/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 869-ReorderedPowerOf2

Difficulty: Medium

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Runtime: 49 ms, faster than 72.19%
        Memory Usage: 13.8 MB, less than 64.17%
        1 <= n <= 10^9
        """
        n = str(n)
        cnt = Counter(n)
        x, MAX = 1, 10 ** 9
        while x <= MAX:
            tmp = str(x)
            if len(tmp) > len(n):
                return False
            elif len(tmp) == len(n) and Counter(tmp) == cnt:
                return True
            x <<= 1
        return False


def test():
    assert Solution().reorderedPowerOf2(n=1)
    assert Solution().reorderedPowerOf2(n=2041)
    assert not Solution().reorderedPowerOf2(n=10)


if __name__ == '__main__':
    test()
