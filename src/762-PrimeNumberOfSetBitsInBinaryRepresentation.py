#!/usr/bin/env python
"""
CREATED AT: 2022/4/5
Des:
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""
from functools import lru_cache


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        Runtime: 108 ms, faster than 98.30%
        Memory Usage: 14 MB, less than 11.76%

        1 <= left <= right <= 10^6
        0 <= right - left <= 10^4

        :param left:
        :param right:
        :return:
        """

        @lru_cache(None)
        def isPrime(num: int) -> bool:
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True

        ret = 0
        for num in range(left, right + 1):
            if isPrime(num.bit_count()):
                ret += 1
        return ret


def test():
    pass


if __name__ == '__main__':
    test()
