#!/usr/bin/env python3
"""
CREATED AT: 2022-08-11

URL: https://leetcode.com/problems/reformat-the-string/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1417-ReformatTheString

Difficulty: Easy

Desc: 

Tag: 

See: 

"""
from tool import *


class Solution:
    def reformat(self, s: str) -> str:
        """
        Runtime: 45 ms, faster than 93.85%
        Memory Usage: 14 MB, less than 46.41%

        1 <= s.length <= 500
        s consists of only lowercase English letters and/or digits.
        """
        d, l = [], []
        for c in s:
            if c in string.digits:
                d.append(c)
            else:
                l.append(c)
        if abs(len(d) - len(l)) > 1:
            return ""
        ret = []
        for x, y in zip(d, l):
            ret.append(x)
            ret.append(y)
        if len(d) > len(l):
            ret.append(d[-1])
        elif len(d) < len(l):
            ret.insert(0, l[-1])
        return "".join(ret)


def test():
    assert Solution().reformat(s="a0b1c2") == "0a1b2c"
    assert Solution().reformat(s="leetcode") == ""
    assert Solution().reformat(s="1229857369") == ""


if __name__ == '__main__':
    test()
