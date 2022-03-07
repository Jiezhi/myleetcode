#!/usr/bin/env python
"""
CREATED AT: 2022/3/7
Des:

https://leetcode.com/problems/wildcard-matching/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: 

See: 

"""
from functools import lru_cache


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        """
        Runtime: 609 ms, faster than 75.68%
        Memory Usage: 108.2 MB, less than 25.75%

        0 <= s.length, p.length <= 2000
        s contains only lowercase English letters.
        p contains only lowercase English letters, '?' or '*'.
        """
        # make sure no adjacent '*'
        pre_len = -1
        curr_len = len(p)
        while curr_len != pre_len:
            pre_len = curr_len
            p = p.replace("**", "*")
            curr_len = len(p)

        @lru_cache(None)
        def dp(i, j) -> bool:
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            if p[j] == '*':
                if dp(i, j + 1):
                    return True
            if i == len(s):
                return False
            if p[j] in [s[i], '?']:
                return dp(i + 1, j + 1)
            elif p[j] == '*':
                return dp(i + 1, j)

            return False

        return dp(0, 0)


def test():
    assert Solution().isMatch("aa", "a") == False
    assert Solution().isMatch("aa", "*") == True
    assert Solution().isMatch(s="cb", p="?a") == False


if __name__ == '__main__':
    test()
