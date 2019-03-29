#!/usr/bin/env python
"""
https://leetcode.com/problems/climbing-stairs/description/
Created on 2018-11-16

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        last = 1
        sum = 1
        for i in range(n - 1):
            tmp = sum
            sum = last + sum
            last = tmp
        return sum


def test():
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
