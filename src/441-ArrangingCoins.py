#!/usr/bin/env python
"""
CREATED AT: 2021/11/5
Des:

https://leetcode.com/problems/arranging-coins/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Runtime: 924 ms, faster than 35.91%
        Memory Usage: 14.3 MB, less than 39.42%
        1 <= n <= 2^31 - 1
        :param n:
        :return:
        """
        i = 1
        while n >= i:
            n, i = n - i, i + 1
        return i - 1


def test():
    assert Solution().arrangeCoins(n=1) == 1
    assert Solution().arrangeCoins(n=2) == 1
    assert Solution().arrangeCoins(n=3) == 2
    assert Solution().arrangeCoins(n=4) == 2
    assert Solution().arrangeCoins(n=5) == 2
    assert Solution().arrangeCoins(n=6) == 3
    assert Solution().arrangeCoins(n=7) == 3
    assert Solution().arrangeCoins(n=8) == 3
    assert Solution().arrangeCoins(n=9) == 3
    assert Solution().arrangeCoins(n=10) == 4


if __name__ == '__main__':
    test()
