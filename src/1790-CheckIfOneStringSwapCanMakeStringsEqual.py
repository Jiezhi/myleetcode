#!/usr/bin/env python3
"""
CREATED AT: 2022-10-11

URL: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

GITHUB: https://github.com/Jiezhi/myleetcode

FileName: 1790-CheckIfOneStringSwapCanMakeStringsEqual

Difficulty: Easy

Desc: 

Tag: 

See: 

"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Runtime: 33 ms, faster than 93.25%
        Memory Usage: 14 MB, less than 20.11%

        1 <= s1.length, s2.length <= 100
        s1.length == s2.length
        s1 and s2 consist of only lowercase English letters.
        """
        i, j = 0, len(s1) - 1
        while i < j and s1[i] == s2[i]:
            i += 1
        while i < j and s1[j] == s2[j]:
            j -= 1
        if i == j:
            return s1[i] == s2[i]
        return s1[i] == s2[j] and s1[j] == s2[i] and s1[i + 1: j] == s2[i + 1:j]


def test():
    assert Solution().areAlmostEqual(s1="bank", s2="kanb")
    assert not Solution().areAlmostEqual(s1="attack", s2="defend")
    assert Solution().areAlmostEqual(s1="kelb", s2="kelb")


if __name__ == '__main__':
    test()
