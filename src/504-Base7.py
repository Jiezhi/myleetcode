#!/usr/bin/env python
"""
CREATED AT: 2022/3/7
Des:

https://leetcode.com/problems/base-7/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        Runtime: 72 ms, faster than 5.39%
        Memory Usage: 13.9 MB, less than 78.10%

        -10^7 <= num <= 10^7
        """
        if num == 0:
            return '0'
        neg = False
        if num < 0:
            neg = True
            num = -num

        ret = []
        while num:
            num, left = divmod(num, 7)
            ret.append(str(left))
        ret = ''.join(ret[::-1])
        return ret if not neg else f'-{ret}'


def test():
    assert Solution().convertToBase7(100) == '202'
    assert Solution().convertToBase7(-7) == '-10'


if __name__ == '__main__':
    test()
