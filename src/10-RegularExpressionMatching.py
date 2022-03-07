#!/usr/bin/env python
"""
CREATED AT: 2021/11/18
Des:

https://leetcode.com/problems/regular-expression-matching/
GITHUB: https://github.com/Jiezhi/myleetcode

Difficulty: Hard

Tag: DP

See: 
"""
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        """
        Solved at 2022/3/7
        Ref: https://leetcode.com/problems/regular-expression-matching/solution/
        Runtime: 42 ms, faster than 93.55%
        Memory Usage: 16.1 MB, less than 5.01%

        1 <= s.length <= 20
        1 <= p.length <= 30
        s contains only lowercase English letters.
        p contains only lowercase English letters, '.', and '*'.
        It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
        """
        if not s and not p:
            return True

        if not p:
            return False

        if len(p) > 1 and p[1] == '*':
            if self.isMatch(s, p[2:]):
                return True

        if s and (s[0] == p[0] or p[0] == '.'):
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s[1:], p)
            else:
                return self.isMatch(s[1:], p[1:])
        return False


def test():
    assert not Solution().isMatch(s="aa", p="a")
    assert Solution().isMatch(s="aa", p="a*")
    assert Solution().isMatch(s="ab", p=".*")
    assert Solution().isMatch(s="aab", p="c*a*b")
    assert not Solution().isMatch(s="mississippi", p="mis*is*p*.")


if __name__ == '__main__':
    test()
