#!/usr/bin/env python
"""
https://leetcode.com/problems/sqrtx/description/
Created on 2018-11-15

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
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
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
