#!/usr/bin/env python
"""
CREATED AT: 2022/2/20
Des:
https://leetcode.com/problems/count-integers-with-even-digit-sum/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def countEven(self, num: int) -> int:
        """
        71 / 71 test cases passed.
        Status: Accepted
        Runtime: 54 ms
        Memory Usage: 13.9 MB
        1 <= num <= 1000
        """

        def sum_even(num):
            ret = 0
            while num > 0:
                num, left = divmod(num, 10)
                ret += left
            return ret % 2 == 0

        ret = 0
        for i in range(1, num + 1):
            if sum_even(i):
                ret += 1
        return ret


def test():
    assert Solution().countEven(num=4) == 2
    assert Solution().countEven(num=30) == 14


if __name__ == '__main__':
    test()
