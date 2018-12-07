#!/usr/bin/env python
"""
https://leetcode.com/problems/string-to-integer-atoi/
Created on 2018-12-04

@author: 'Jiezhi.G@gmail.com'

Reference: 
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        match = re.match(r'[-|+]?\d+', str.strip())
        if not match:
            return 0
        num = int(match.group())
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if num < - 2 ** 31:
            return -2 ** 31
        return num


if __name__ == '__main__':
    assert Solution().myAtoi('42') == 42
    assert Solution().myAtoi('   -42') == -42
    assert Solution().myAtoi('4193 with words') == 4193
    assert Solution().myAtoi('words and 987') == 0
    assert Solution().myAtoi('-91283472332') == -2147483648
    assert Solution().myAtoi('+1') == 1
    pass
