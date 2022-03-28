#!/usr/bin/env python
"""
CREATED AT: 2022/3/28
Des:
https://leetcode.com/problems/binary-number-with-alternating-bits/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        """
        Runtime: 35 ms, faster than 73.50%
        Memory Usage: 13.9 MB, less than 13.66%
        
        :param n: 1 <= n <= 2^31 - 1
        :return:
        """
        b = n & 1
        while n != 0:
            n >>= 1
            if (n & 1) == b:
                return False
            b = n & 1
        return True


def test():
    assert Solution().hasAlternatingBits(5)
    assert not Solution().hasAlternatingBits(14)


if __name__ == '__main__':
    test()
