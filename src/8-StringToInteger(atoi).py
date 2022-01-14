#!/usr/bin/env python
"""
https://leetcode.com/problems/string-to-integer-atoi/
Created on 2018-12-04

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Runtime: 32 ms, faster than 86.58%
        Memory Usage: 14.2 MB, less than 81.95%

        :type str: str
        :rtype: int
        """

        match = re.match(r'[-|+]?\d+', s.strip())
        if not match:
            return 0
        num = int(match.group())
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if num < - 2 ** 31:
            return -2 ** 31
        return num


def test():
    assert Solution().myAtoi('42') == 42
    assert Solution().myAtoi('   -42') == -42
    assert Solution().myAtoi('4193 with words') == 4193
    assert Solution().myAtoi('words and 987') == 0
    assert Solution().myAtoi('-91283472332') == -2147483648
    assert Solution().myAtoi('+1') == 1


if __name__ == '__main__':
    test()
