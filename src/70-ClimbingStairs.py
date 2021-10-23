#!/usr/bin/env python
"""
https://leetcode.com/problems/climbing-stairs/description/
Created on 2018-11-16
Updated on 2021-10-05

@author: 'Jiezhi.G@gmail.com'

Reference: More solution can refer to https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/2377/

Difficulty: Easy
"""
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        """
        Updated on 2021-10-05, Using DP
        45 / 45 test cases passed.
        Status: Accepted
        Runtime: 55 ms
        Memory Usage: 14.4 MB
        :param n:
        :return:
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n):
        """
        45 / 45 test cases passed.
        Status: Accepted
        Runtime: 24 ms
        Memory Usage: 13.9 MB
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
    assert Solution().climbStairs(45) == 1836311903
    assert Solution().climbStairs2(45) == 1836311903


if __name__ == '__main__':
    test()
