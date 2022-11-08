#!/usr/bin/env python3
"""
CREATED AT: 2022-11-08

URL: https://leetcode.com/problems/make-the-string-great/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1544-MakeTheStringGreat

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def makeGood(self, s: str) -> str:
        """
        Runtime: 91 ms, faster than 8.21%
        Memory Usage: 13.9 MB, less than 15.06%
        1 <= s.length <= 100
        s contains only lower and upper case English letters.
        """
        s = list(s)
        cur, pre = len(s), 0
        while cur != pre:
            pre = cur
            i = 0
            while i < len(s) - 1:
                if s[i] != s[i + 1] and s[i].lower() == s[i + 1].lower():
                    s.pop(i)
                    s.pop(i)
                else:
                    i += 1
            cur = len(s)
        return ''.join(s)


def test():
    assert Solution().makeGood(s="leEeetcode") == "leetcode"
    assert Solution().makeGood(s="abBAcC") == ""


if __name__ == '__main__':
    test()
