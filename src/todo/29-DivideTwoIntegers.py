#!/usr/bin/env python
"""
CREATED AT: 2021/10/17
Des:

https://leetcode.com/problems/divide-two-integers/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Medium

Tag: 

See: 
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        -2**31 <= dividend, divisor <= 2**31 - 1
        divisor != 0
        :param dividend:
        :param divisor:
        :return:
        """
        if dividend == 0:
            return 0
        negative = False
        # Turn all num to negative
        if divisor < 0 and dividend > 0:
            negative = True
            dividend = -dividend
        elif divisor > 0 and dividend < 0:
            negative = True
            divisor = -divisor
        elif divisor > 0 and dividend > 0:
            divisor = -divisor
            dividend = -dividend

        ret = 1
        # all num are negative now
        if dividend > divisor:
            return 0
        while divisor > dividend:
            divisor += divisor
            ret += 1
        if negative and divisor == dividend:
            return -ret
        return -ret + 1 if negative else ret


def test():
    assert Solution().divide(dividend=-1, divisor=2) == 0
    assert Solution().divide(dividend=1, divisor=2) == 0
    assert Solution().divide(dividend=-1, divisor=1) == -1
    assert Solution().divide(dividend=10, divisor=3) == 3
    assert Solution().divide(dividend=5, divisor=2) == 2
    assert Solution().divide(dividend=7, divisor=-3) == -2
    assert Solution().divide(dividend=0, divisor=-3) == 0
    assert Solution().divide(dividend=1, divisor=1) == 1
    assert Solution().divide(dividend=1, divisor=-1) == -1
    assert Solution().divide(dividend=-1, divisor=-1) == 1


if __name__ == '__main__':
    test()
