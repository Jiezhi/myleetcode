#!/usr/bin/env python
"""
CREATED AT: 2021/10/12
Des:

https://leetcode.com/problems/is-subsequence/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Easy
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Runtime: 40 ms, faster than 38.47%
        Memory Usage: 14.2 MB, less than 74.32%
        0 <= s.length <= 100
        0 <= t.length <= 104
        :param s:
        :param t:
        :return:
        """
        if len(s) == 0:
            return True
        index = 0
        for c in t:
            if s[index] == c:
                index += 1
            if index == len(s):
                return True
        return False


def test():
    assert not Solution().isSubsequence(s='b', t='c')
    assert Solution().isSubsequence(s="abc", t="ahbgdc")
    assert not Solution().isSubsequence(s="axc", t="ahbgdc")


if __name__ == '__main__':
    test()
