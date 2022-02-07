#!/usr/bin/env python
"""
CREATED AT: 2022/2/7
Des:

https://leetcode.com/problems/find-the-difference/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy

Tag: 

See: 

Time Spent:  min
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Runtime: 44 ms, faster than 51.20%
        Memory Usage: 14 MB, less than 79.84%
        0 <= s.length <= 1000
        t.length == s.length + 1
        s and t consist of lowercase English letters.
        :param s:
        :param t:
        :return:
        """
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]


def test():
    assert Solution().findTheDifference(s="abcd", t="abcde") == "e"
    assert Solution().findTheDifference(s="abcd", t="acebd") == "e"
    assert Solution().findTheDifference(s="", t="y") == "y"


if __name__ == '__main__':
    test()
