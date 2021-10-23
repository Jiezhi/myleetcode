#!/usr/bin/env python
"""
Github: https://github.com/Jiezhi/myleetcode

Created on 2019-08-14

Leetcode:  https://leetcode.com/problems/powx-n/

"""


class Solution:
    # FIXME
    def myPow(self, x: float, n: int) -> float:
        # return pow(x, n)
        def helper(x, n, acc):
            if n == 0:
                return acc
            return helper(x, n - 1, acc * x)

        if n > 0:
            return helper(x, n, 1)
        else:
            return helper(1 / x, -n, 1)

    def myPow1(self, x: float, n: int):
        if n == 0:
            return 1
        if abs(x - 0.0) < 0.0000001:
            return 0.0
        if abs(x - 1.0) < 0.0000001:
            return 1.0
        if n % 2 == 0:
            return pow(x * x, n / 2)
        else:
            return x * pow(x * x, n / 2)

    # Fixme
    def myPow2(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        acc = 1
        for _ in range(n):
            acc *= x
        return acc


def test():
    assert Solution().myPow1(2.0, 10) == 1024.0000
    assert Solution().myPow1(2.0, -2) == 0.25

    assert Solution().myPow2(2.0, 10) == 1024.0000
    assert Solution().myPow2(2.0, -2) == 0.25


if __name__ == '__main__':
    # print(pow(1.00001, 123456))
    # print(Solution().myPow1(1.00001, 123456))
    # print(pow(0.00001, 2147483647))
    test()
