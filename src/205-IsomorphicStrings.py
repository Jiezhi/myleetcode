#!/usr/bin/env python3
"""
CREATED AT: 2022-08-08

URL: https://leetcode.com/problems/isomorphic-strings/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 205-IsomorphicStrings

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Runtime: 79 ms, faster than 28.68%
        Memory Usage: 14.3 MB, less than 18.94%
        1 <= s.length <= 5 * 10^4
        t.length == s.length
        s and t consist of any valid ascii character.
        """

        def is_ok(s: str, t: str) -> bool:
            dct = {}
            for i in range(len(s)):
                if s[i] in dct:
                    if dct[s[i]] != t[i]:
                        return False
                else:
                    dct[s[i]] = t[i]
            return True

        return is_ok(s, t) and is_ok(t, s)


def test():
    assert not Solution().isIsomorphic(s="badc", t="baba")
    assert Solution().isIsomorphic(s="egg", t="add")
    assert not Solution().isIsomorphic(s="foo", t="bar")
    assert Solution().isIsomorphic(s="paper", t="title")


if __name__ == '__main__':
    test()
