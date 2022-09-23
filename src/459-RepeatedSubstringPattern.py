#!/usr/bin/env python3
"""
CREATED AT: 2022-09-23

URL: https://leetcode.com/problems/repeated-substring-pattern/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 459-RepeatedSubstringPattern

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Runtime: 77 ms, faster than 65.20%
        Memory Usage: 14 MB, less than 61.49%

        1 <= s.length <= 10^4
        s consists of lowercase English letters.
        """
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0 and s.count(s[:i]) * i == len(s):
                return True
        return False


def test():
    assert Solution().repeatedSubstringPattern(s="abab")
    assert not Solution().repeatedSubstringPattern(s="aba")
    assert Solution().repeatedSubstringPattern(s="abcabcabcabc")


if __name__ == '__main__':
    test()
