#!/usr/bin/env python
"""
https://leetcode.com/problems/sqrtx/description/
GITHUB: https://github.com/Jiezhi/myleetcode
Created on 2018-11-15

@author: 'Jiezhi.G@gmail.com'

Difficulty: Easy

Tag: BS

Reference: 
"""


class Solution:
    def mySqrt2(self, x: int) -> int:
        """
        Updated at 2021/12/02
        1017 / 1017 test cases passed.
        Status: Accepted
        Runtime: 32 ms
        Memory Usage: 14.3 MB
        0 <= x <= 2^31 - 1
        :param x:
        :return:
        """
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        return low - 1

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        low = 0
        high = x
        while low < high - 1:
            mid = low + (high - low) // 2
            ret = mid * mid
            if ret == x:
                return mid
            if ret > x:
                high = mid
            else:
                low = mid
        return low


def test():
    assert Solution().mySqrt2(1) == 1
    assert Solution().mySqrt2(2) == 1
    assert Solution().mySqrt2(4) == 2
    assert Solution().mySqrt2(8) == 2

    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2


if __name__ == '__main__':
    test()
