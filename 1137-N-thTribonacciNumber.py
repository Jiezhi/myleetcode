#!/usr/bin/env python
"""
CREATED AT: 2021/9/24
Des:
https://leetcode.com/problems/n-th-tribonacci-number
https://leetcode.com/explore/item/3986
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def tribonacci(self, n: int) -> int:
        """
        39 / 39 test cases passed.
        Status: Accepted
        Runtime: 24 ms
        Memory Usage: 14.5 MB
        :param n:
        :return:
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


def test():
    assert Solution().tribonacci(n=4) == 4
    assert Solution().tribonacci(n=25) == 1389537
    assert Solution().tribonacci(n=37) == 2082876103


if __name__ == '__main__':
    test()
