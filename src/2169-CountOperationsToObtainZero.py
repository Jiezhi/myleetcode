#!/usr/bin/env python
"""
CREATED AT: 2022/2/13
Des:
https://leetcode.com/problems/count-operations-to-obtain-zero
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        """
        0 <= num1, num2 <= 10^5
        """
        ret = 0
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            ret += 1
        return ret


def test():
    assert Solution().countOperations(num1=2, num2=3) == 3


if __name__ == '__main__':
    test()
