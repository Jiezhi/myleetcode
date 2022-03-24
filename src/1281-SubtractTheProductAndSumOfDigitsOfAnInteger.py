#!/usr/bin/env python
"""
CREATED AT: 2022/3/24
Des:
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        Runtime: 21 ms, faster than 98.95%
        Memory Usage: 13.9 MB, less than 58.95%

        1 <= n <= 10^5
        """
        p, s = 1, 0
        while n != 0:
            n, left = divmod(n, 10)
            p *= left
            s += left
        return p - s


def test():
    assert Solution().subtractProductAndSum(234) == 15
    assert Solution().subtractProductAndSum(4421) == 21


if __name__ == '__main__':
    test()
