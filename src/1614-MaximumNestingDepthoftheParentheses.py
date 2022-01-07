#!/usr/bin/env python
"""
CREATED AT: 2022/1/7
Des:

https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Runtime: 37 ms, faster than 22.52%
        Memory Usage: 14 MB, less than 97.97%


        1 <= s.length <= 100
        s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
        It is guaranteed that parentheses expression s is a VPS.
        :param s:
        :return:
        """
        ret = 0
        tmp_max = 0
        for c in s:
            if c == '(':
                tmp_max += 1
            elif c == ')':
                if tmp_max >= ret:
                    ret = tmp_max
                tmp_max -= 1
        return ret


def test():
    assert Solution().maxDepth(s="(1+(2*3)+((8)/4))+1") == 3
    assert Solution().maxDepth(s="(1)+((2))+(((3)))") == 3


if __name__ == '__main__':
    test()
