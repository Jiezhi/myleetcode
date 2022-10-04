#!/usr/bin/env python3
"""
CREATED AT: 2022-10-04

URL: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 921-MinimumAddToMakeParenthesesValid

Difficulty: Medium

Desc: 

Tag: 

See: 

"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Runtime: 64 ms, faster than 19.60%
        Memory Usage: 13.9 MB, less than 10.51%

        1 <= s.length <= 1000
        s[i] is either '(' or ')'.
        """
        ret, stack = 0, 0
        for c in s:
            if c == '(':
                stack += 1
            elif stack:
                stack -= 1
            else:
                ret += 1
        return ret + stack


def test():
    assert Solution().minAddToMakeValid(s=")))(((") == 6
    assert Solution().minAddToMakeValid(s="())") == 1
    assert Solution().minAddToMakeValid(s="(((") == 3


if __name__ == '__main__':
    test()
