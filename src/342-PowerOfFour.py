#!/usr/bin/env python
"""
CREATED AT: 2022/3/16
Des:

https://leetcode.com/problems/power-of-four/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Runtime: 24 ms, faster than 99.32%
        Memory Usage: 13.8 MB, less than 66.90%

        -2^31 <= n <= 2^31 - 1
        """
        if n <= 0:
            return False
        num = 1
        while num <= n:
            if num == n:
                return True
            num *= 4
        return False


def test():
    assert Solution().isPowerOfFour(16)
    assert not Solution().isPowerOfFour(3)


if __name__ == '__main__':
    test()
