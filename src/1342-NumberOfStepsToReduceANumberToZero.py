#!/usr/bin/env python
"""
CREATED AT: 2022/5/27
Des:
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        Runtime: 71 ms, faster than 5.24%
        Memory Usage: 13.7 MB, less than 99.82%
        :param num:  0 <= num <= 10^6
        :return:
        """
        ret = 0
        while num != 0:
            ret += 1
            if num & 1 == 0:
                num //= 2
            else:
                num -= 1
        return ret


def test():
    assert Solution().numberOfSteps(14) == 6


if __name__ == '__main__':
    test()
