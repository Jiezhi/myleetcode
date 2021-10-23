#!/usr/bin/env python
"""
CREATED AT: 2021/10/7
Des:
https://leetcode.com/problems/ugly-number/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        """
        1013 / 1013 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.4 MB
        :param n:
        :return:
        """
        while True:
            if n == 1:
                return True
            if n == 0:
                return False
            elif n % 2 == 0:
                n = n / 2
            elif n % 3 == 0:
                n = n / 3
            elif n % 5 == 0:
                n = n / 5
            else:
                return False


def test():
    assert not Solution().isUgly(n=0)
    assert Solution().isUgly(n=1)
    assert Solution().isUgly(n=6)
    assert Solution().isUgly(n=15)
    assert Solution().isUgly(8)
    assert not Solution().isUgly(14)


if __name__ == '__main__':
    test()
